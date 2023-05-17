import "../../css/settings/settings.moudule.css";
import "../../css/settings/active.moudule.css";
import React, { useState, useContext } from "react";
import { useNavigate } from "react-router-dom";
import { FileNameContext } from "../../App";

const options = [
  {
    label: "1",
    value: "C:/Users/ilaya/LaunchVideos/VideoBefore/MissileLaunch1",
  },
  {
    label: "2",
    value: "C:/Users/ilaya/LaunchVideos/VideoBefore/MissileLaunch2",
  },
  {
    label: "3",
    value: "C:/Users/ilaya/LaunchVideos/VideoBefore/MissileLaunch3",
  },
  {
    label: "4",
    value: "C:/Users/ilaya/LaunchVideos/VideoBefore/MissileLaunch4",
  },
  {
    label: "5",
    value: "C:/Users/ilaya/LaunchVideos/VideoBefore/MissileLaunch5",
  },
];

const SettingsApp = () => {
  const [inputValue, setInputValue] = useState(null);
  const navigate = useNavigate();
  const { isActive, setIsActive } = useContext(FileNameContext);
  const Swal = require("sweetalert2");

  const handleRadioButtonChange = (event) => {
    setIsActive(event.target.value === "active");
  };
  console.log("active : ", isActive);
  let urlVideo;
  let socket;

  const onClickLaunch = () => {
    let response = false;
    console.log("response", response);
    urlVideo = localStorage.getItem("urlStream");
    socket = new WebSocket("ws://localhost:3005/ws/stream/");
    socket.onopen = function (event) {
      console.log("inputValue", inputValue);
      socket.send(
        JSON.stringify({
          url: isActive ? inputValue.value : urlVideo,
          active: isActive,
        })
      );
      socket.onmessage = (event) => {
        const data = JSON.parse(event.data);
        if (data.message === "Received Url and Active successfully!") {
          response = true;
          localStorage.setItem("activeAlgorithm", isActive);
          localStorage.setItem("urlStream", inputValue.value);
          console.log("data in settings page:", data);
          Swal.fire({
            position: "row",
            icon: "success",
            title: "Settings submitted successfully",
            showConfirmButton: true,
            confirmButtonText: "Keep To Live Stream",
            showCancelButton: true,
            cancelButtonText: "Change the settings",
          }).then((result) => {
            if (result.isConfirmed) {
              navigate("/live");
            } else {
              navigate("/settings");
            }
          });
        }
      };
    };
    socket.onerror = (event) => {
      console.log(event);
      Swal.fire({
        position: "row",
        icon: "error",
        title: `WebSocket connection failed `,
        showConfirmButton: true,
        confirmButtonText: "Check Server Details",
      });
    };
  };

  return (
    <div class="card">
      <div className="h1Container">
        <h1 className="h1">Settings Page</h1>
      </div>

      <div className="containerActive">
        <div className="radio-input">
          <input
            name="activeOrInactive"
            type="radio"
            value="active"
            className="input"
            checked={isActive}
            onChange={handleRadioButtonChange}
          />
          <span className="span"></span>
          Active
        </div>
        <div className="radio-input">
          <input
            name="activeOrInactive"
            type="radio"
            value="inactive"
            className="input"
            checked={!isActive}
            onChange={handleRadioButtonChange}
          />
          <span className="span"></span>
          Inactive
        </div>
      </div>
      <div>
        <div className="h4Container">
          <h4 className="h4">Select Stream</h4>
        </div>
      </div>
      <div class="container">
        <div>
          <div className="h4ContainerActive">
            <h4 className="h4active">Use Algorithm</h4>
          </div>
        </div>
        <div class="de">
          <div class="den">
            <hr class="line" />
            <hr class="line" />
            <hr class="line" />
            <div class="switch">
              <label htmlFor="switch_off">
                <span>Stream</span>
              </label>
              {options.map((option, index) => (
                <label key={index} htmlFor={`switch_${index + 1}`}>
                  <span>{option.label}</span>
                </label>
              ))}
              <input type="radio" checked name="switch" id="switch_off" />
              <input
                type="radio"
                name="switch"
                id="switch_1"
                onChange={() => {
                  setInputValue(options[0]);
                  localStorage.setItem("urlStream", inputValue.value);
                }}
              />
              <input
                type="radio"
                name="switch"
                id="switch_2"
                onChange={() => {
                  setInputValue(options[1]);
                  localStorage.setItem("urlStream", inputValue.value);
                }}
              />
              <input
                type="radio"
                name="switch"
                id="switch_3"
                onChange={() => {
                  setInputValue(options[2]);
                  localStorage.setItem("urlStream", inputValue.value);
                }}
              />
              <input
                type="radio"
                name="switch"
                id="switch_4"
                onChange={() => {
                  setInputValue(options[3]);
                  localStorage.setItem("urlStream", inputValue.value);
                }}
              />
              <input
                type="radio"
                name="switch"
                id="switch_5"
                onChange={() => {
                  setInputValue(options[4]);
                  localStorage.setItem("urlStream", inputValue.value);
                }}
              />
              <div class="light">
                <span></span>
              </div>
              <div class="dot">
                <span></span>
              </div>
              <div class="dene">
                <div class="denem">
                  <div class="deneme"></div>
                </div>
              </div>
            </div>
            <div class="contatinerSetButton">
              <div>
                <button class="setButton" onClick={onClickLaunch}>
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 24 24"
                    width="24"
                    height="24"
                  >
                    <path fill="none" d="M0 0h24v24H0z"></path>
                    <path
                      fill="currentColor"
                      d="M5 13c0-5.088 2.903-9.436 7-11.182C16.097 3.564 19 7.912 19 13c0 .823-.076 1.626-.22 2.403l1.94 1.832a.5.5 0 0 1 .095.603l-2.495 4.575a.5.5 0 0 1-.793.114l-2.234-2.234a1 1 0 0 0-.707-.293H9.414a1 1 0 0 0-.707.293l-2.234 2.234a.5.5 0 0 1-.793-.114l-2.495-4.575a.5.5 0 0 1 .095-.603l1.94-1.832C5.077 14.626 5 13.823 5 13zm1.476 6.696l.817-.817A3 3 0 0 1 9.414 18h5.172a3 3 0 0 1 2.121.879l.817.817.982-1.8-1.1-1.04a2 2 0 0 1-.593-1.82c.124-.664.187-1.345.187-2.036 0-3.87-1.995-7.3-5-8.96C8.995 5.7 7 9.13 7 13c0 .691.063 1.372.187 2.037a2 2 0 0 1-.593 1.82l-1.1 1.039.982 1.8zM12 13a2 2 0 1 1 0-4 2 2 0 0 1 0 4z"
                    ></path>
                  </svg>
                  <span>Launch</span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default SettingsApp;
// import React from 'react';
// import axios from "axios";
// import Swal from 'sweetalert2';
// import Button from "react-bootstrap/Button";
// import * as FaIcons from 'react-icons/fa';
// import styles from './css/UploadFile.module.scss';
// import "bootstrap/dist/css/bootstrap.min.css";
// function FileUpload({addFile}) {

//     const uploadFile = async (e) => {
//         const { value: file } = await Swal.fire({
//             title: 'העלאת קובץ הקלטת טיסה',
//             input: 'file',
//             inputValidator: (fileName) => {
//                 return new Promise((resolve) => {
//                   if (fileName === null) {
//                     resolve("יש לבחור קובץ להעלאה");
//                   }

//                   else if (fileName['type'].split('/')[0] !== 'text') {
//                       resolve("!בחר קובץ בפורמט טקסט להעלאה")
//                   }
//                   else {
//                       resolve();
//                   }
//                 })
//               },
//             inputAttributes: {
//               'accept': 'text/plain',
//             },
//             confirmButtonText: "העלה קובץ",
//             showCancelButton: true,
//             cancelButtonText: 'בטל'
//           });

//         console.log(typeof file)
//         if(file && typeof file !== "undefined") {
//             console.log("===upload file====");
//             console.log(file);
//             const formData = new FormData(); //
//             formData.append("formFile", file);
//             formData.append("fileName", file.name);

//             try {
//               const uploadFileRes = await axios.post("api/uploadFile", formData);
//               console.log("======try to parse file and save in the C# server=======");
//               console.log(uploadFileRes.data);

//                var data = [];
//                for (let [key, value] of Object.entries(uploadFileRes.data)) {
//                  data.push({
//                     TimeStamp: key,
//                     Bus: value.Bus,
//                     Cmd: value.CMD,
//                     MessageType: value.MessageType,
//                     AllData: value.Data
//                   })
//               }

//                const MongoDbObject = {
//                  fileName: file.name,
//                  dateTime: Date(),
//                  data: data
//                }

//                console.log(MongoDbObject);

//                 const uploadMongoDbRes = await axios.post("api/recordingFile", MongoDbObject,
//                 { headers: { 'Content-Type': 'application/json; charset=utf-8'}});

//                console.log("======try upload to MongoDB======");
//                console.log(uploadMongoDbRes);
//                addFile(MongoDbObject);

//               Swal.fire({icon: 'success', showConfirmButton: false, timer: 2000,
//               title: file.name + " הקובץ" + "\n" + "!הועלה בהצלחה"});

//             }

//             catch(ex) {
//                 console.log(ex);
//                 Swal.fire({icon: 'error',
//                 title: '!העלאת קובץ ההקלטה נכשלה', text: '.בדוק שהקובץ שבחרת להעלאה הוא אכן קובץ הקלטה'});
//             }
//         }
//     }

//     return (
//       <>
//           <Button className={styles.FileUploadBtn} onClick={uploadFile}>
//             <FaIcons.FaFileUpload/> העלה קובץ
//           </Button>
//         </>
//     )
// }

// export default FileUpload;
