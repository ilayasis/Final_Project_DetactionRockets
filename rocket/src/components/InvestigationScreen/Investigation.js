import React, { useRef, useEffect, useState, useContext } from "react";
import cssVideo from "../../css/InvestigationScreen/Investigation.module.css";
import { FileNameContext } from "../../App";
import { toByteArray } from "base64-js";
import ReactPlayer from "react-player";
import RocketLoading from "../LaunchSections/RocketLoading";

const Investigation = () => {
  const [videoDataFromDB, setVideoDataFromDB] = useState("");
  const { videoData } = useContext(FileNameContext);
  const playerRef = useRef(null);
  const [playbackRate, setPlaybackRate] = useState(1);
  const prevVideoData = useRef(null);

  const [markers, setMarkers] = useState([]);
  const [progress, setProgress] = useState(0);
  const [currentMarker, setCurrentMarker] = useState(null);
  const videoRef = useRef(null);

  const [currentTime, setCurrentTime] = useState(0);
  const [confidence, setConfidence] = useState(0);
  const [surface, setSurface] = useState(0);
  const [coordinates, setCoordinates] = useState(0);

  function handleVideoProgress(state) {
    setProgress(state.played);
    // find the marker that matches the current time
    const currentMarkerIndex = markers.findIndex((marker) => {
      const timeDiff = Math.abs(marker.time - state.playedSeconds);
      const threshold = 0.01; // adjust this as needed
      return timeDiff < threshold;
    });
    setCurrentMarker(
      currentMarkerIndex > -1 ? markers[currentMarkerIndex] : null
    );
  }

  // useEffect(() => {
  //   handleVideoProgress();
  // }, []);

  const handleMarkerClick = (marker) => {
    if (playerRef.current) {
      playerRef.current.seekTo(marker.time);
      console.log(`Marker at ${marker.time} seconds`);
      const currentTime = playerRef.current.getCurrentTime();
      console.log("time in the video : ", currentTime);
    }
  };
  const handleNextFrame = () => {
    const currentTime = playerRef.current.getCurrentTime();
    const duration = playerRef.current.getDuration();
    const fps = 30; // assuming 30 frames per second
    playerRef.current.seekTo(Math.min(currentTime + 1 / fps, duration));
  };

  const handlePreviousFrame = () => {
    const currentTime = playerRef.current.getCurrentTime();
    const fps = 30; // assuming 30 frames per second
    playerRef.current.seekTo(Math.max(currentTime - 1 / fps, 0));
  };

  const handlePlaybackRateChange = (rate) => {
    setPlaybackRate(rate);
    playerRef.current.setPlaybackRate(rate);
  };

  const fetchData = async () => {
    try {
      const response = await fetch(
        `http://127.0.0.1:8000/load_video?filename=${videoData}`
      );
      if (response) {
        const data = await response.json();
        // access the video and detection data fields
        // const video = data.video;
        console.log("data", data);
        const detectionData = data.Data;
        const video = data.video;
        const videoBytes = toByteArray(video);
        // create a Blob from the video data
        const videoBlob = new Blob([videoBytes], { type: "video/mp4" });
        const videoUrl = URL.createObjectURL(videoBlob);

        // setVideoDataa(`http://127.0.0.1:8000/load_video?filename=${videoData}`);

        console.log("videoUrl", videoUrl);

        // parse the detection data JSON string into a JavaScript object
        const detectionDataObj = JSON.parse(detectionData);
        // const dataArray = Object.entries(detectionDataObj);
        const newMarkers = detectionDataObj.map((detection) => ({
          time: detection.time,
          surface_area: detection.surface_area,
          confidence: detection.confidence,
          coordinates: detection.coordinates,
        }));
        setMarkers(newMarkers);
        console.log("newMarkers", newMarkers);
        // access the values in the detection data (e.g. console.log them)
        console.log(detectionDataObj);
        console.log("dataMarkers");
        setVideoDataFromDB(videoUrl);
      } else {
        throw new Error(`Fetch failed with status ${response.status}`);
      }
    } catch (error) {
      console.error(error);
    }
  };

  function updateDataNow(
    markers,
    setCurrentTime,
    setConfidence,
    setSurface,
    setCoordinates
  ) {
    markers.forEach((marker) => {
      if (marker === currentMarker) {
        setCurrentTime(marker.time);
        setConfidence(marker.confidence);
        setSurface(marker.surface_area);
        setCoordinates(marker.coordinates);
      }
    });
  }

  useEffect(() => {
    if (videoData && videoData !== prevVideoData.current) {
      fetchData();
      console.log("videoDataa", videoDataFromDB);
    }
    console.log("videoDataa", videoDataFromDB);
    prevVideoData.current = videoDataFromDB;
  }, [videoData]);

  return (
    <div>
      {videoDataFromDB ? (
        <div>
          <div>
            <ReactPlayer
              width="650px"
              height="650px"
              className={cssVideo.cardVideo}
              style={{
                position: "absolute",
                bottom: "-54%",
                transform: "translateY(-50%)",
                margin: "130px 390px",
              }}
              ref={playerRef}
              url={videoDataFromDB}
              controls={true}
              playIcon={<button>Play</button>}
              disablePictureInPicture={true}
              config={{
                file: {
                  attributes: {
                    controlsList: "nodownload",
                  },
                  tracks: markers.map((marker, index) => ({
                    kind: "metadata",
                    src: "",
                    srclang: "",
                    default: index === 0,
                    cues: [
                      {
                        startTime: marker.time,
                        endTime: marker.time,
                      },
                    ],
                  })),
                },
              }}
              onProgress={(state) => handleVideoProgress(state)}
              renderMarker={({ marker }) => (
                <div
                  style={{
                    position: "absolute",
                    top: "50%",
                    left: `calc(${
                      (marker.time / (playerRef.current?.getDuration() || 1)) *
                      100
                    }%)`,
                    transform: "translateY(-50%)",
                    width: "10px",
                    height: "10px",
                    borderRadius: "40%",
                    backgroundColor: "red",
                    cursor: "pointer",
                  }}
                  onClick={() => handleMarkerClick(marker)}
                  onMouseEnter={() =>
                    console.log(`Marker at ${marker.time} seconds`)
                  }
                />
              )}
            />
          </div>
          <div>
            {markers.map((marker, index) => (
              <div
                key={index}
                style={{
                  position: "absolute",
                  left:
                    (marker.time / (playerRef.current?.getDuration() || 1)) *
                      660 +
                    390 +
                    "px",
                  // marginLeft: "390px",
                  top: "95%",
                  width: "5px",
                  height: "5px",
                  borderRadius: "100%",
                  backgroundColor: "red",
                  cursor: "pointer",
                }}
                onClick={() => {
                  console.log(marker.time, playerRef.current.getDuration());
                  handleMarkerClick(marker);
                }}
              />
            ))}
          </div>
          <div>
            <button onClick={handlePreviousFrame}>Previous Frame</button>
            <button onClick={handleNextFrame}>Next Frame</button>
          </div>
          <div className={cssVideo.secondAnimation}>
            <div className={cssVideo.card}>
              {markers.map(
                (marker) =>
                  marker === currentMarker && (
                    <div key={marker.time}>
                      {/* <h4>{marker.time}</h4> */}
                      <h4>Confidence : {marker.confidence} </h4>
                      <h4>Surface area : {marker.surface_area} </h4>
                      <h4>Coordinates: {marker.coordinates} </h4>
                    </div>
                  )
              )}
            </div>
          </div>
        </div>
      ) : (
        <RocketLoading />
      )}
    </div>
  );
};

export default Investigation;

// function handleVideoProgress(state) {
//   setProgress(state.played);
//   markers.forEach((marker) => {
//     if (
//       state.playedSeconds >= marker.time &&
//       state.playedSeconds < marker.time + 1
//     ) {
//       setCurrentMarker(marker);
//     }
//   });
// }
// function handleVideoProgress(state) {
//   setProgress(state.played);
//   // loop through all markers and display additional data for markers close to the current time
//   markers.forEach((marker) => {
//     const timeDiff = Math.abs(marker.time - state.playedSeconds);
//     const threshold = 0.01; // adjust this as needed
//     if (timeDiff < threshold) {
//       console.log(
//         `Marker at ${marker.time} seconds: surface area = ${marker.surface_area}, confidence = ${marker.confidence}`
//       );
//     }
//   });
// }

// function handleVideoProgress(state) {
//   setProgress(state.played);
//   // loop through all markers and display additional data for markers close to the current time
//   const currentMarkers = markers.filter((marker) => {
//     const timeDiff = Math.abs(marker.time - state.playedSeconds);
//     const threshold = 0.01; // adjust this as needed
//     return timeDiff < threshold;
//   });
//   setCurrentMarker(currentMarkers[0]); // assume only one marker can match the current time
// }

// useEffect(() => {
//   // Your code to fetch and update markers goes here
//   // ...

//   // Set the current marker based on some logic
//   setCurrentMarker(markers[0]);
// }, []);
// // useEffect(() => {
// //   // Update the current marker based on some logic
// //   // ...

// //   // Force a re-render of the component to update the <div>
// //   setCurrentMarker(currentMarker);
// // }, [currentMarker]);

// onProgress={handleVideoProgress}
// onProgress={({ playedSeconds }) => {
//   const duration = playerRef.current?.getDuration() || 1;
//   setProgress((playedSeconds / duration) * 100);
// }}

// const handleVideoProgress = (state) => {
//   const currentTime = state.playedSeconds;
//   const duration = playerRef.current.getDuration();
//   markers.forEach((marker, index) => {
//     const markerTime = marker.time;
//     const markerElement = document.getElementById(`marker-${index}`);
//     const newLeft = `${(markerTime / duration) * 100}%`;
//     markerElement.style.left = newLeft;
//   });
// };
// useEffect(() => {
//   function MarkerDisplay({ markers, currentMarker }) {
//     return (
//       <div className={cssVideo.card}>
//         {markers.map(
//           (marker) =>
//             marker === currentMarker && (
//               <div key={marker.time}>
//                 <h4>Confidence : {marker.confidence} </h4>
//                 <h4>Surface area : {marker.surface_area} </h4>
//                 <h4>Coordinates: {marker.coordinates} </h4>
//               </div>
//             )
//         )}
//       </div>
//     );
//   }
// }, []);

// import React, { useRef, useEffect, useState, useContext } from "react";
// import ReactPlayer from "react-player";
// import Video from "../../Video/MissileLaunch1.mp4";
// import css from "../../Main.module.css";
// import cssVideo from "../../css/InvestigationScreen/Investigation.module.css";
// import { FileNameContext } from "../../App";
// import { toByteArray } from "base64-js";
// const Investigation = () => {
//   const [videoDataFromDB, setVideoDataFromDB] = useState("");
//   const { videoData } = useContext(FileNameContext);
//   const playerRef = useRef(null);
//   const [playbackRate, setPlaybackRate] = useState(1);
//   const prevVideoData = useRef(null);

//   const [markers, setMarkers] = useState([]);

//   const handleMarkerClick = (marker) => {
//     if (playerRef.current) {
//       playerRef.current.seekTo(marker.time);
//     }
//   };
//   const handleNextFrame = () => {
//     const currentTime = playerRef.current.getCurrentTime();
//     const duration = playerRef.current.getDuration();
//     const fps = 30; // assuming 30 frames per second
//     playerRef.current.seekTo(Math.min(currentTime + 1 / fps, duration));
//   };

//   const handlePreviousFrame = () => {
//     const currentTime = playerRef.current.getCurrentTime();
//     const fps = 30; // assuming 30 frames per second
//     playerRef.current.seekTo(Math.max(currentTime - 1 / fps, 0));
//   };

//   const handlePlaybackRateChange = (rate) => {
//     setPlaybackRate(rate);
//     playerRef.current.setPlaybackRate(rate);
//   };
//   const fetchData = async () => {
//     try {
//       const response = await fetch(
//         `http://127.0.0.1:8000/load_video?filename=${videoData}`
//       );
//       if (response) {
//         const data = await response.json();
//         // access the video and detection data fields
//         // const video = data.video;
//         console.log("data", data);
//         const detectionData = data.Data;
//         const video = data.video;
//         const videoBytes = toByteArray(video);
//         // create a Blob from the video data
//         const videoBlob = new Blob([videoBytes], { type: "video/mp4" });
//         const videoUrl = URL.createObjectURL(videoBlob);

//         // setVideoDataa(`http://127.0.0.1:8000/load_video?filename=${videoData}`);
//         setVideoDataFromDB(videoUrl);
//         console.log("videoUrl", videoUrl);

//         // parse the detection data JSON string into a JavaScript object
//         const detectionDataObj = JSON.parse(detectionData);
//         // const dataArray = Object.entries(detectionDataObj);
//         setMarkers(detectionDataObj);
//         // access the values in the detection data (e.g. console.log them)
//         console.log(detectionDataObj);
//         console.log("dataMarkers");
//       } else {
//         throw new Error(`Fetch failed with status ${response.status}`);
//       }
//     } catch (error) {
//       console.error(error);
//     }
//   };

//   useEffect(() => {
//     if (videoData && videoData !== prevVideoData.current) {
//       fetchData();
//       console.log("videoDataa", videoDataFromDB);
//     }
//     console.log("videoDataa", videoDataFromDB);
//     prevVideoData.current = videoDataFromDB;
//   }, [videoData]);
//   return (
//     <div>
//       {videoDataFromDB ? (
//         <div>
//           <div>
//             <ReactPlayer
//               width="670px"
//               height="670px"
//               className={cssVideo.card}
//               style={{
//                 position: "absolute",
//                 bottom: "-54%",
//                 transform: "translateY(-50%)",
//                 margin: "130px 390px",
//               }}
//               ref={playerRef}
//               url={videoDataFromDB}
//               controls={true}
//               playIcon={<button>Play</button>}
//               disablePictureInPicture={true}
//               config={{
//                 file: {
//                   attributes: {
//                     controlsList: "nodownload",
//                   },
//                   tracks: markers.map((marker, index) => ({
//                     kind: "metadata",
//                     src: "",
//                     srclang: "",
//                     default: index === 0,
//                     cues: [
//                       {
//                         startTime: marker.time,
//                         endTime: marker.time + 0.01,
//                         text: "",
//                       },
//                     ],
//                   })),
//                 },
//               }}
//               renderMarker={({ marker }) => (
//                 <div
//                   style={{
//                     position: "absolute",
//                     top: "50%",
//                     left: `calc(${
//                       (marker.time / (playerRef.current?.getDuration() || 1)) *
//                       100
//                     }% - 5px)`,
//                     transform: "translateY(-50%)",
//                     width: "10px",
//                     height: "10px",
//                     borderRadius: "50%",
//                     backgroundColor: "red",
//                     cursor: "pointer",
//                   }}
//                   onClick={() => handleMarkerClick(marker)}
//                 />
//               )}
//             />
//           </div>

//           <div>
//             {markers.map((marker, index) => (
//               <div
//                 key={index}
//                 style={{
//                   position: "absolute",
//                   left: `calc(${
//                     (marker.time / (playerRef.current?.getDuration() || 1)) *
//                     100
//                   }% - 5px)`,
//                   transform: "translateY(-50%)",
//                   width: "12px",
//                   height: "12px",
//                   borderRadius: "70%",
//                   backgroundColor: "red",
//                   cursor: "pointer",
//                 }}
//                 onClick={() => handleMarkerClick(marker)}
//               />
//             ))}
//           </div>
//           <div>
//             <button onClick={handlePreviousFrame}>Previous Frame</button>
//             <button onClick={handleNextFrame}>Next Frame</button>
//           </div>
//         </div>
//       ) : (
//         <p> Loading video... </p>
//       )}
//     </div>
//   );
// };

// export default Investigation;
// // import ReactPlayer from 'react-player';

// // const markers = [
// //   { time: 2, text: 'Marker 1' },
// //   { time: 5, text: 'Marker 2' },
// //   { time: 10, text: 'Marker 3' }
// // ];

// // function App() {
// //   return (

// //   );
// // }
