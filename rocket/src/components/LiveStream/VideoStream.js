import React, { useState, useEffect, useContext } from "react";
import { SpinnerDiamond } from "spinners-react";
import LoadingSpinnerButton from "../ButtunSpiner/LoadingSpinnerButton";
import css from "../../Main.module.css";

import { FileNameContext } from "../../App";
const VideoStream = () => {
  const { isActive, setIsActive } = useContext(FileNameContext);
  const [frame, setFrame] = useState(null);
  const [isPlaying, setIsPlaying] = useState(false);
  const [DetConfidence, setDetConfidence] = useState(0);
  const [children, setChildren] = useState([]);
  const [loadBeforeStrem, setShowBeforeStrem] = useState(true);
  const [timeDetect, setTimeDetect] = useState("");
  const date = new Date();
  const showTime =
    date.getHours() + ":" + date.getMinutes() + ":" + date.getSeconds();
  let socket;
  let urlVideo;
  let activeAlgorithm;
  let adminStorage;
  urlVideo = localStorage.getItem("urlStream");
  //

  useEffect(() => {
    if (isPlaying) {
      urlVideo = localStorage.getItem("urlStream");
      adminStorage = localStorage.getItem("admin");
      activeAlgorithm = localStorage.getItem("activeAlgorithm");
      if (activeAlgorithm == "true") {
        activeAlgorithm = true;
      } else {
        activeAlgorithm = false;
      }
      console.log(isActive);
      console.log("adminStorage :", adminStorage);
      if (adminStorage == "false") {
        console.log("hi");
        socket = new WebSocket("ws://localhost:3005/ws/stream/");
        socket.onopen = function (event) {
          socket.send(
            JSON.stringify({
              start: true,
              url: urlVideo,
              active: activeAlgorithm,
            })
          );
        };
      } else {
        socket = new WebSocket("ws://localhost:3005/ws/stream/");
        console.log("adminStorage2 :", adminStorage);
        socket.onopen = function (event) {
          socket.send(
            JSON.stringify({
              start: true,
            })
          );
        };
      }

      socket.onmessage = (event) => {
        const data = JSON.parse(event.data);
        console.log("data:", data);
        const frame = "data:image/jpeg;base64," + data.frame;
        const detection = data.confidence;
        const timeDetect = data.time;
        setFrame(frame);
        setDetConfidence(detection);
        setTimeDetect(timeDetect);
      };
    }
    return () => {
      socket?.close();
      setChildren([]);
    };
  }, [isPlaying]);

  const getBackground = (DetConfidence) => {
    if (DetConfidence > 0.01 && DetConfidence <= 0.2) {
      return "#fec9c9";
    } else if (DetConfidence > 0.2 && DetConfidence <= 0.4) {
      return "#ffa1a1";
    } else if (DetConfidence > 0.4 && DetConfidence <= 0.6) {
      return "#ff8080";
    } else if (DetConfidence > 0.6 && DetConfidence <= 0.8) {
      return "#ff5f5f";
    } else if (DetConfidence > 0.8 && DetConfidence < 1) {
      return "#ff0e0e";
    }
  };
  useEffect(() => {
    if (DetConfidence > 0) {
      setChildren((prev) => [
        <div style={{ backgroundColor: getBackground(DetConfidence) }}>
          <h6>Detection:{DetConfidence}</h6>
          <h6> Cureent Time:{showTime}</h6>
          {/* <h6>Detection:{timeDetect}</h6> */}
        </div>,
        ...prev,
      ]);
    }
  }, [DetConfidence, showTime]);
  const onLoadStart = (event) => {
    event.preventDefault();

    setIsPlaying(!isPlaying);
    /* Time taken by API to send data */
    setTimeout(() => {
      setShowBeforeStrem(false);
    }, 2500);
  };

  return (
    <div>
      <div className={css.spiner}>
        <LoadingSpinnerButton
          title={isPlaying ? "Stop" : "Start"}
          isPlaying={isPlaying}
          onClick={onLoadStart}
        />
      </div>
      <button onClick={() => setIsPlaying(!isPlaying)}>
        {isPlaying ? "Stop" : "Start"}
      </button>
      {isPlaying ? (
        <img className={css.img} src={frame} alt="Stream" />
      ) : (
        <div className={css.imgload}>
          <SpinnerDiamond
            style={{ marginLeft: 320, marginTop: 150 }}
            size={150}
            thickness={121}
            speed={90}
            color="rgba(110, 57, 172, 0.81)"
            secondaryColor="rgba(57, 172, 154, 1)"
          />
        </div>
      )}
      <div>
        <div className={css.cat}>{children}</div>
      </div>
    </div>
  );
};

export default VideoStream;
