import React, { useState, useRef, useEffect } from "react";
import cssVideo from "../../css/FileData/FileData.module.css";
import { toByteArray } from "base64-js";
import ReactPlayer from "react-player";
import design from "../../css/FileData/Waiting.module.css";

const FileData = ({ activeFile, resetActiveFile }) => {
  const playerRef = useRef(null);
  const [markers, setMarkers] = useState([]);
  const [start, setStart] = useState(false);
  const [timeData, setTimeData] = useState([]);
  const [surfaceAreaData, setSurfaceAreaData] = useState([]);
  const [confidenceData, setConfidenceData] = useState([]);
  const [coordinatesData, setCoordinatesData] = useState([]);
  const [xmin, setXmin] = useState([]);
  const [ymin, setYmin] = useState([]);
  const [xmax, setXmax] = useState([]);
  const [ymax, setYmax] = useState([]);
  const [playerLoaded, setPlayerLoaded] = useState(false);
  const [videoUrl, setVideoUrl] = useState();
  const detectionData = activeFile?.Data;
  const video = activeFile?.video;
  const videoBytes = toByteArray(video);
  const FPS = 30; // set the video frame rate
  const [children, setChildren] = useState([]);
  // create a Blob from the video data
  useEffect(() => {
    const videoBytes = toByteArray(video);
    const videoBlob = new Blob([videoBytes], { type: "video/mp4" });
    const url = URL.createObjectURL(videoBlob);
    setVideoUrl(url);
  }, []);

  const handleMarkerClick = (marker) => {
    if (playerRef.current) {
      playerRef.current.seekTo(marker.time);
      console.log(`Marker at ${marker.time} seconds`);
      const currentTime = playerRef.current.getCurrentTime();
      console.log("time in the video : ", currentTime);
    }
  };
  // const [displayData, setDisplayData] = useState({
  //   surfaceArea: null,
  //   confidence: null,
  //   coordinates: null,
  //   time: null,
  // });
  // parse the detection data JSON string into a JavaScript object
  const detectionDataObj = JSON.parse(detectionData);

  useEffect(() => {
    const newMarkers = detectionDataObj.map((detection, index) => {
      setTimeData((prevTimeData) => [...prevTimeData, detection.time]);
      setSurfaceAreaData((prevSurfaceAreaData) => [
        ...prevSurfaceAreaData,
        detection.surface_area,
      ]);
      setConfidenceData((prevConfidenceData) => [
        ...prevConfidenceData,
        detection.confidence,
      ]);
      setCoordinatesData((prevCoordinatesData) => [
        ...prevCoordinatesData,
        detection.coordinates,
      ]);
      setXmin((prevXmin) => [...prevXmin, detection.xmin]);
      setYmin((prevYmin) => [...prevYmin, detection.ymin]);
      setXmax((prevXmax) => [...prevXmax, detection.xmax]);
      setYmax((prevYmax) => [...prevYmax, detection.ymax]);

      // calculate the timecode value for each marker based on its frame number
      const timecode = index - 1 / FPS;

      return {
        time: detection.time,
        surface_area: detection.surface_area,
        confidence: detection.confidence,
        coordinates: detection.coordinates,
        xmin: detection.xmin,
        ymin: detection.ymin,
        xmax: detection.xmax,
        ymax: detection.ymax,
        timecode: timecode,
      };
    });

    setMarkers(newMarkers);
    renderMarkers();
  }, []);

  if (!activeFile) {
    return null;
  }

  const handleVideoProgress = (state) => {
    // if (!isPlaying) {
    //   setIsPlaying(true);
    // }
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

  const renderMarkers = (currentTime) => {
    markers
      .filter((marker) => marker.time - currentTime < 0.02)
      .map((marker) =>
        setChildren((prevChildren) => [
          <div className={cssVideo.DataCard}>
            <h3
              style={{ borderBottom: "1px solid black", width: "28%" }}
              className={cssVideo.Detection}
            >
              Detection <br />
            </h3>
            <h4 className={cssVideo.DetectionData}>{marker.confidence}</h4>

            <h3
              style={{ borderBottom: "1px solid black", width: "37%" }}
              className={cssVideo.SurfaceArea}
            >
              Surface Area <br />
            </h3>
            <h4 className={cssVideo.DetectionData}>{marker.surface_area}</h4>
            <h3
              style={{ borderBottom: "1px solid black", width: "37%" }}
              className={cssVideo.SurfaceArea}
            >
              Coordinates
              <br />
            </h3>
            <div className={cssVideo.firstPoint}>
              <h6 className={cssVideo.DetectionData}>
                <h6 className={cssVideo.pointsOne}>xmin,ymin</h6>({marker.xmin},{" "}
                {marker.ymin})
              </h6>
            </div>

            <div className={cssVideo.secondPoint}>
              <h6 className={cssVideo.DetectionData}>
                <h6 className={cssVideo.pointsTwo}>xmin,ymax</h6>({marker.xmin},{" "}
                {marker.ymax})
              </h6>
            </div>

            <div className={cssVideo.thirdPoint}>
              <h6 className={cssVideo.DetectionData}>
                <h6 className={cssVideo.pointsThree}>xmax,ymin</h6>(
                {marker.xmax}, {marker.ymin})
              </h6>
            </div>
            <div className={cssVideo.fourPoint}>
              <h6 className={cssVideo.DetectionData}>
                <h6 className={cssVideo.pointFour}>xmax,ymax</h6>({marker.xmax},
                {marker.ymax})
              </h6>
            </div>
          </div>,
          ...prevChildren,
        ])
      );
  };

  {
    /* <h6 className={cssVideo.DetectionData}>{marker.xmin}</h6>
            <h4 className={cssVideo.DetectionData}>{marker.ymin}</h4>
            <h4 className={cssVideo.DetectionData}>{marker.xmax}</h4>
            <h4 className={cssVideo.DetectionData}>{marker.ymax}</h4> */
  }
  return (
    <div>
      <div className={cssVideo.cardFile}>
        <div
          className={cssVideo.buttonFilesContainer}
          onClick={resetActiveFile}
        >
          <button className={cssVideo.buttonFiles}>
            <svg
              height="16"
              width="16"
              xmlns="http://www.w3.org/2000/svg"
              version="1.1"
              viewBox="0 0 1024 1024"
            >
              <path d="M874.690416 495.52477c0 11.2973-9.168824 20.466124-20.466124 20.466124l-604.773963 0 188.083679 188.083679c7.992021 7.992021 7.992021 20.947078 0 28.939099-4.001127 3.990894-9.240455 5.996574-14.46955 5.996574-5.239328 0-10.478655-1.995447-14.479783-5.996574l-223.00912-223.00912c-3.837398-3.837398-5.996574-9.046027-5.996574-14.46955 0-5.433756 2.159176-10.632151 5.996574-14.46955l223.019353-223.029586c7.992021-7.992021 20.957311-7.992021 28.949332 0 7.992021 8.002254 7.992021 20.957311 0 28.949332l-188.073446 188.073446 604.753497 0C865.521592 475.058646 874.690416 484.217237 874.690416 495.52477z"></path>
            </svg>
            <span> </span>
          </button>
        </div>
        <div className={cssVideo.h5Container}>
          <h5 className={cssVideo.h5}>Investigation System</h5>
        </div>
        <div className={cssVideo.cardData}>{children}</div>

        <ReactPlayer
          onReady={() => setPlayerLoaded(true)}
          width="540px"
          height="540px"
          className={cssVideo.cardVideo}
          style={{
            position: "absolute",
            bottom: "-54%",
            transform: "translateY(-50%)",
            margin: "180px 220px 190px 20px",
          }}
          ref={playerRef}
          url={videoUrl}
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
          onProgress={(state) => {
            const currentTime = state.playedSeconds;
            renderMarkers(currentTime);
          }}
        />

        <div>
          {markers.map((marker, index) => (
            <div
              key={index}
              style={{
                position: "absolute",
                left:
                  (marker.time / (playerRef.current?.getDuration() || 1)) *
                    510 +
                  29 +
                  "px",
                // marginLeft: "390px",
                top: "92.9%",
                width: "5px",
                height: "12px",
                borderRadius: "100%",
                backgroundColor: "red",
                cursor: "pointer",
              }}
              onClick={() => {
                console.log(marker.time);
                handleMarkerClick(marker);
              }}
            />
          ))}
        </div>

        <div className={cssVideo["line-container"]}>
          <div className={cssVideo["line-connector"]}></div>
        </div>
        <div style={{ position: "relative" }}>
          <button
            className={cssVideo.buttonLastFrame}
            onClick={handlePreviousFrame}
          >
            Previous Frame
          </button>
          <button
            className={cssVideo.buttonNextFrame}
            onClick={handleNextFrame}
          >
            Next Frame
          </button>
        </div>
      </div>
    </div>
  );
};

export default FileData;

// const renderMarkers = (currentTime) => {
//   const filteredMarkers = markers.filter(
//     (marker) => marker.time - currentTime < 0.02
//   );
//   console.log(filteredMarkers);

//   if (filteredMarkers.length === 0) {
//     return setChildren((prevChildren) => [
//       <div key="pending" className={design.animation}>
//         Pending investigation start
//       </div>,
//     ]);
//   } else {
//     return filteredMarkers.map((marker) =>
//       setChildren((prevChildren) => [
//         <div className={cssVideo.DataCard}>
//           <h3
//             style={{ borderBottom: "1px solid black", width: "28%" }}
//             className={cssVideo.Detection}
//           >
//             Detection <br />
//           </h3>
//           <h4 className={cssVideo.DetectionData}>{marker.confidence}</h4>

//           <h3
//             style={{ borderBottom: "1px solid black", width: "37%" }}
//             className={cssVideo.SurfaceArea}
//           >
//             Surface Area <br />
//           </h3>
//           <h4 className={cssVideo.DetectionData}>{marker.surface_area}</h4>
//           <h3
//             style={{ borderBottom: "1px solid black", width: "37%" }}
//             className={cssVideo.SurfaceArea}
//           >
//             Coordinates
//             <br />
//           </h3>
//           <div className={cssVideo.firstPoint}>
//             <h6 className={cssVideo.DetectionData}>
//               <h6 className={cssVideo.pointsOne}>xmin,ymin</h6>({marker.xmin},{" "}
//               {marker.ymin})
//             </h6>
//           </div>

//           <div className={cssVideo.secondPoint}>
//             <h6 className={cssVideo.DetectionData}>
//               <h6 className={cssVideo.pointsTwo}>xmin,ymax</h6>({marker.xmin},{" "}
//               {marker.ymax})
//             </h6>
//           </div>

//           <div className={cssVideo.thirdPoint}>
//             <h6 className={cssVideo.DetectionData}>
//               <h6 className={cssVideo.pointsThree}>xmax,ymin</h6>(
//               {marker.xmax}, {marker.ymin})
//             </h6>
//           </div>
//           <div className={cssVideo.fourPoint}>
//             <h6 className={cssVideo.DetectionData}>
//               <h6 className={cssVideo.pointFour}>xmax,ymax</h6>({marker.xmax},
//               {marker.ymax})
//             </h6>
//           </div>
//         </div>,
//         ...prevChildren,
//       ])
//     );
//   }
// };
