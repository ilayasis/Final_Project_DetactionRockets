import React, { useState, useEffect, useContext } from "react";
import { FileNameContext } from "../../App";
import { SpinnerDiamond } from "spinners-react";
// import css from "../../Main.module.css";
import { useNavigate } from "react-router-dom";
import design from "../../css/LiveStream/Live.moudule.css";
import alertSound from "../../assets/audio/alert.mp3";

const LiveStream = () => {
  const audio = new Audio(alertSound);
  const { isActive, setIsActive } = useContext(FileNameContext);
  const navigate = useNavigate();
  const [frame, setFrame] = useState(null);
  const [isPlaying, setIsPlaying] = useState(false);
  const [DetConfidence, setDetConfidence] = useState(0);
  const [children, setChildren] = useState([]);
  const [buttonClick, SetButtonClick] = useState(false);
  const Swal = require("sweetalert2");

  let socket;
  let urlVideo;
  let activeAlgorithm;
  let adminStorage;
  urlVideo = localStorage.getItem("urlStream");
  useEffect(() => {
    if (buttonClick) {
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
              // url: urlVideo,
              // active: activeAlgorithm,
            })
          );
        };
      }

      socket.onmessage = (event) => {
        const data = JSON.parse(event.data);
        console.log("data:", data);
        if (data.frame) {
          const frame = "data:image/jpeg;base64," + data.frame;
          const detection = data.confidence;
          setFrame(frame);
          setDetConfidence(detection);
          setIsPlaying(data.streamOn);
        }
        setIsPlaying(data.streamOn);
        if (data.streamOn === false && adminStorage == "true") {
          Swal.fire({
            position: "row",
            icon: "success",
            title: "Streaming completed successfully",
            showConfirmButton: true,
            confirmButtonText: "Keep To Investigation screen",
            showCancelButton: true,
            cancelButtonText: "Change Stream Video",
            showDenyButton: "true",
            denyButtonText: "Stay In live Stream",
          }).then((result) => {
            if (result.isConfirmed) {
              setChildren([]);
              navigate("/investigation");
            }
            if (result.isDismissed) {
              navigate("/settings");
            }
            if (result.isDenied) {
              navigate("/live");
            }
          });
          SetButtonClick(false);
        }
        if (data.streamOn === false && adminStorage == "false") {
          Swal.fire({
            position: "row",
            icon: "success",
            title: "Streaming completed successfully",
            showConfirmButton: true,
            confirmButtonText: "Keep To Investigation screen",
            showDenyButton: "true",
            denyButtonText: "Stay In live Stream",
          }).then((result) => {
            if (result.isConfirmed) {
              setChildren([]);
              navigate("/investigation");
            }
            if (result.isDenied) {
              navigate("/live");
            }
          });
          SetButtonClick(false);
        }
      };
    }

    return () => {
      // socket?.close();
      // setChildren([]);
    };
  }, [buttonClick]);

  //background div Data
  const getBackground = (DetConfidence) => {
    if (DetConfidence > 0.01 && DetConfidence < 0.2) {
      return "#fec9c9";
    } else if (DetConfidence >= 0.2 && DetConfidence < 0.4) {
      return "#ffa1a1";
    } else if (DetConfidence >= 0.4 && DetConfidence < 0.6) {
      return "#ff8080";
    } else if (DetConfidence >= 0.6 && DetConfidence < 0.8) {
      return "#ff5f5f";
    } else if (DetConfidence >= 0.8 && DetConfidence < 1) {
      return "#ff0e0e";
    }
  };

  //Show Time
  const date = new Date();
  const day = date.getDate();
  const month = date.getMonth() + 1; // Add 1 to get the correct month (January is 0)
  const hours = date.getHours();
  const minutes = date.getMinutes();
  const seconds = date.getSeconds();
  const showTime = `${day}/${
    month < 10 ? `0${month}` : month
  } - ${hours}:${minutes}:${seconds}`;

  useEffect(() => {
    if (DetConfidence > 0) {
      // audio.play();
      setChildren((prev) => [
        <div
          className="cardStreamData"
          style={{
            backgroundColor: getBackground(DetConfidence),
            height: "140px",
            marginBottom: "10px",
            width: "202px",
            marginLeft: "3px",
            marginTop: "2px",
            border: "solid 2px",
          }}
        >
          <h3
            style={{
              marginLeft: "50px",
              borderBottom: "1px solid black",
              width: "58%",
              fontFamily: "serif",
              marginTop: "2px",
            }}
            className="confidenceData"
          >
            Detection <br />
          </h3>
          <h4 className="confidence">{DetConfidence}</h4>
          <h3
            style={{
              marginLeft: "32px",
              borderBottom: "1px solid black",
              width: "71%",
            }}
            className="timeHead"
          >
            Cureent Time <br />
          </h3>
          <h4 className="timeText">{showTime}</h4>
        </div>,
        ...prev,
      ]);
    }
  }, [DetConfidence, showTime]);

  return (
    <div>
      <div className="datac">
        <div className="containerr">
          <div className="textContainer">
            <h1 className="text">Live Stream</h1>
          </div>
        </div>
        {!isPlaying ? (
          <button
            className="buttonLive"
            onClick={() => {
              SetButtonClick(true);
            }}
          >
            Start Live Stream
          </button>
        ) : (
          ""
        )}

        {isPlaying ? (
          <img className="img" src={frame} alt="Stream" />
        ) : (
          <div className="imgloading">
            <SpinnerDiamond
              style={{ marginLeft: 320, marginTop: 150 }}
              size={150}
              thickness={121}
              speed={90}
              color="#111"
              secondaryColor="rgba(57, 172, 154, 1)"
            />
          </div>
        )}
        <div>
          <div className="detectiondata">{children}</div>
        </div>
        <div>
          {DetConfidence > 0 ? (
            <div className="loader">
              <span></span>
            </div>
          ) : null}
        </div>
      </div>
    </div>
  );
};

export default LiveStream;
