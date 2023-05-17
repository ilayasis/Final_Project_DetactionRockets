import React, { useRef, useEffect, useState, useContext } from "react";
import { FileNameContext } from "../App";
import VideoPlayer from "react-video-player-extended";
import css from "../../Main.module.css";
import { toByteArray } from "base64-js";

const InvestigationVideo = () => {
  const [videoDataa, setVideoDataa] = useState("");
  const { videoData } = useContext(FileNameContext);
  const [isPlaying, setIsPlaying] = React.useState(false);
  const [volume, setVolume] = React.useState(0.7);
  const [currentTime, setCurrentTime] = useState(0);
  const prevVideoData = useRef(null);

  const videoRef = useRef(null);
  // const videoRef = React.createRef();

  const handleTimeUpdate = (time) => {
    setCurrentTime(time);
  };

  const markers = [
    { time: 0.39, name: "Chapter 1" },
    { time: 1, name: "Chapter 2" },
    { time: 6, name: "Chapter 3" },
  ];

  const handleMarkerClick = (marker) => {
    videoRef.current.seekTo(marker.time);
  };

  const handlePlay = () => {
    setIsPlaying(true);
  };

  const handlePause = () => {
    setIsPlaying(false);
  };

  const handleVolume = (value) => {
    setVolume(value);
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
        const detectionData = data.Data;
        const video = data.video;
        const videoBytes = toByteArray(video);
        // create a Blob from the video data
        const videoBlob = new Blob([videoBytes], { type: "video/mp4" });
        const videoUrl = URL.createObjectURL(videoBlob);

        // setVideoDataa(`http://127.0.0.1:8000/load_video?filename=${videoData}`);
        setVideoDataa(videoUrl);
        console.log("videoUrl", videoUrl);

        // parse the detection data JSON string into a JavaScript object
        const detectionDataObj = JSON.parse(detectionData);

        // access the values in the detection data (e.g. console.log them)
        console.log(detectionDataObj);
      } else {
        throw new Error(`Fetch failed with status ${response.status}`);
      }
    } catch (error) {
      console.error(error);
    }
  };

  useEffect(() => {
    if (videoData && videoData !== prevVideoData.current) {
      fetchData();
      console.log("videoDataa", videoDataa);
    }
    console.log("videoDataa", videoDataa);
    prevVideoData.current = videoData;
  }, [videoData]);

  return (
    <div className={css.container}>
      {videoDataa ? (
        <div className={css.container}>
          <VideoPlayer
            url={videoDataa}
            currentTime={currentTime}
            onTimeUpdate={handleTimeUpdate}
            isPlaying={isPlaying}
            volume={volume}
            onPlay={handlePlay}
            onPause={handlePause}
            onVolume={handleVolume}
            markers={markers}
            onMarkerClick={handleMarkerClick}
            ref={videoRef}
            onCanPlay={() => videoRef.current.play()}
          />
        </div>
      ) : (
        <p> Loading video... </p>
      )}
    </div>
  );
};
export default InvestigationVideo;
