// import React, { useEffect, useState, useRef } from "react";
// import css from "./Main.module.css";
// import axios from "axios";
// import { SpinnerDiamond } from "spinners-react";
// import socketIOClient from "socket.io-client";
// import LoadingSpinnerButton from "./components/ButtunSpiner/LoadingSpinnerButton";

// import io from "socket.io-client";

// const Streamvideo = () => {
//   const urlStream = "http://127.0.0.1:8000/video_feed/";
//   // const urlTest = "http://127.0.0.1:8000/data";
//   const urlDetaction = "http://127.0.0.1:8000/detection_percentage/";
//   // const change = useRef(null);
//   const [data, setData] = useState("");
//   const [children, setChildren] = useState([]);
//   const [isRunning, setIsRunning] = useState(true);
//   const [loading, setLoading] = useState(false);
//   const [click, setClick] = useState(false);
//   const [loadBeforeStrem, setShowBeforeStrem] = useState(true);
//   const [confidence, setConfidence] = useState(null);
//   const [socket, setSocket] = useState(null);
//   const [ws, setWs] = useState(null);
//   const [message, setMessage] = useState("");
//   const date = new Date();
//   const showTime =
//     date.getHours() + ":" + date.getMinutes() + ":" + date.getSeconds();

//   let flag = isRunning;
//   const start = -0.1;

//   const onLoadStart = (event) => {
//     event.preventDefault();

//     setLoading(true);
//     setClick(true);
//     /* Time taken by API to send data */
//     setTimeout(() => {
//       setLoading(false);
//       setShowBeforeStrem(false);
//     }, 1000);
//   };

//   const getDetection = async () => {
//     let flag = isRunning;
//     // const start = isToggled;
//     while (click && flag) {
//       console.log("before try isRunning,flag,start", isRunning, flag);
//       // console.log("in while buttonIsOn", buttonIsOn);
//       try {
//         const resp = await axios.get(urlDetaction);
//         //urlDetaction  = "http://127.0.0.1:8000/detection_percentage/"
//         console.log(resp);
//         let flag = resp.data.isRunning;
//         // console.log("in try buttonIsOn", buttonIsOn);
//         if (!isNaN(resp.data.det)) {
//           setData(resp.data.det);
//           // setData(start);
//           console.log("detection", resp.data.det);
//         }
//         if (flag === false) {
//           console.log("in flag start", flag);
//           break;
//         }
//       } catch (err) {
//         console.error(err);
//       }
//     }
//   };

//   useEffect(() => {
//     if (data > 0) {
//       setChildren((prev) => [
//         <div style={{ backgroundColor: getBackground(data) }}>
//           <h6>Detection:{data}</h6>
//           <h6> Cureent Time:{showTime}</h6>
//         </div>,
//         ...prev,
//       ]);
//     }
//   }, [data, showTime]);

//   const getBackground = (data) => {
//     if (data > 0.01 && data <= 0.2) {
//       return "#fec9c9";
//     } else if (data > 0.2 && data <= 0.4) {
//       return "#ffa1a1";
//     } else if (data > 0.4 && data <= 0.6) {
//       return "#ff8080";
//     } else if (data > 0.6 && data <= 0.8) {
//       return "#ff5f5f";
//     } else if (data > 0.8 && data < 1) {
//       return "#ff0e0e";
//     }
//   };

//   return (
//     <div>
//       <div className={css.spiner}>
//         <LoadingSpinnerButton
//           title={"Load Data"}
//           loading={loading}
//           onClick={onLoadStart}
//         />
//       </div>
//       <img className={css.img} src={urlStream} alt="stream" />
//       {click ? (
//         <img className={css.img} src={urlStream} alt="stream" />
//       ) : (
//         <div className={css.imgload}>
//           <SpinnerDiamond
//             style={{ marginLeft: 320, marginTop: 150 }}
//             size={150}
//             thickness={121}
//             speed={90}
//             color="rgba(110, 57, 172, 0.81)"
//             secondaryColor="rgba(57, 172, 154, 1)"
//           />
//         </div>
//       )}
//       {/* <ClipLoader
//           className={css.img}
//           loading={loadBeforeStrem}
//           size={150}
//           aria-label="Loading Spinner"
//           data-testid="loader"
//         /> */}
//       <div>
//         <div className={css.cat}>{children}</div>
//       </div>
//     </div>
//   );
// };

// export default Streamvideo;

// // import React, { useEffect, useRef } from "react";
// // import css from "./Main.module.css";
// // const Streamvideo = () => {
// //   const videoRef = useRef(null);
// //   const urlStream = "http://127.0.0.1:8000/video_feed/";

// //   useEffect(() => {
// //     const fetchStream = async () => {
// //       const response = await fetch(urlStream, {
// //         method: "POST",
// //         headers: {
// //           "Content-Type": "application/x-www-form-urlencoded",
// //         },
// //         body: `url=${encodeURIComponent(urlStream)}`,
// //       });

// //       const reader = response.body.getReader();
// //       const stream = new ReadableStream({
// //         start(controller) {
// //           const pump = () => {
// //             reader.read().then(({ done, value }) => {
// //               if (done) {
// //                 controller.close();
// //                 return;
// //               }
// //               controller.enqueue(value);
// //               pump();
// //             });
// //           };

// //           pump();
// //         },
// //       });

// //       if (stream instanceof MediaStream) {
// //         videoRef.current.srcObject = stream;
// //       } else {
// //         console.error("Invalid media stream");
// //       }
// //     };

// //     fetchStream();
// //   }, []);

// //   return (
// //     <div>
// //       <video ref={videoRef} />
// //     </div>
// //   );
// // };

// // export default Streamvideo;

// // import Snackbar from "./components/Snackbar/Snackbar";
// // // import LoadStream from "./components/LoadStream/LoadStream";
// // import nodePickle from "node-pickle";
// // import jsonpickle from "jsonpickle";
// // import Switch from "./components/Button/Switch";
// // // import Switch from "@mui/material/Switch";
// // // import styled from "styled-components";
// // // import buttonmodule from "./css/buttunOnOff/OnOff.module.css";
// // import ClipLoader from "react-spinners/ClipLoader";
// // const SnackbarType = {
// //   success: "success",
// //   fail: "fail",
// // };

// // axios.get(urlTest).then((response) => {
// //   jsonpickle.decode(response.data.img).then((data) => {
// //     console.log("data", data);
// //   });
// // });
// // console.log(a);
// // setVideo(a.data.vid);

// // <SpinnerCircular
// // size={50}
// // thickness={100}
// // speed={100}
// // color="#36ad47"
// // secondaryColor="rgba(0, 0, 0, 0.44)"
// // />

// // let buttonIsOn = !checked;
// // const handleChange = (event) => {
// //   setChecked(event.target.checked);
// //   console.log("first", checked);
// // };
// //
// //
// /* <div>
//         <ToggleButton isOn={isOn} handle={handleToggle} />
//       </div>

// const [isOn, setIsOn] = useState(false);

//   const handleToggle = () => {
//     setIsOn(!isOn);
//   };
//   const ToggleButton = ({ isOn, handle }) => {
//     return <Toggle isOn={isOn} onClick={handle} />;
//   };

// const Toggle = styled.div`
//   width: 90px;
//   height: 40px;
//   margin: 10px 900px;
//   display: flex;
//   aligh-items: center;
//   cursor: pointer;
//   position: relative;
//   background-color: ${(props) => (props.isOn === true ? "green" : "black")};
//   transition: background-color 500ms linear;

//   border-raduis: 30px;

//   &:before {
//     content: "${(props) => (props.isOn === true ? "|" : "O")}";
//     width: 35px;
//     height: 35px;
//     background-color: white;
//     border-raduis: 50%;
//     margin: 0 2px;
//     display: flex;
//     aligh-items: center;
//     justify-content: center;
//     position: absolute;
//     left: ${(props) => (props.isOn === true ? "51px" : "0")};
//     transition: left 500ms linear;
//   }
// `; */

// // */

// // // const getDetection = () => {
// //   Promise.all([axios.get(urlDetaction)])
// //     .then((response) => {
// //       console.log(response[0]);
// //       const data = response[0].data;
// //       // console.log(data);
// //       setData(data);
// //     })
// //     .catch((error) => {
// //       console.log(error);
// //     });
// // };

// // {/* <div>
// // {
// //   /* <button className={css.button} onclick={handleClick}>
// // Start Stream
// // </button>
// // </div> */
// // }

// <Route
//               path="/user/*"
//               element={
//                 <PrivateRoutes component={User} token={token} isAdmin={admin} />
//               }
//             />

//             <Route
//               path="/adduser"
//               element={
//                 <PrivateRoutes
//                   component={AddUser}
//                   token={token}
//                   isAdmin={admin}
//                 />
//               }
//             />

//             <Route
//               path="/live"
//               element={<PrivateRoutes component={VideoSream} token={token} />}
//             />
//             <Route
//               path="/settings"
//               element={
//                 <PrivateRoutes
//                   component={Settings}
//                   token={token}
//                   isAdmin={admin}
//                 />
//               }
//             />
//             <Route
//               path="/investigation"
//               element={<PrivateRoutes component={Videos} token={token} />}
//             />
//             <Route
//               path="/InvestigationVideo"
//               element={
//                 <PrivateRoutes component={Investigation} token={token} />
//               }
//             />
//           </Route>

// export default App;

// import React, { useEffect, useState, useRef } from "react";
// import css from "./Main.module.css";
// import axios from "axios";
// import { SpinnerDiamond } from "spinners-react";
// import LoadingSpinnerButton from "./components/ButtunSpiner/LoadingSpinnerButton";

// const Streamvideo = () => {
//   const urlStream = "http://127.0.0.1:8000/video_feed/";
//   // const urlTest = "http://127.0.0.1:8000/data";
//   const urlDetaction = "http://127.0.0.1:8000/detection_percentage/";
//   // const change = useRef(null);
//   const [data, setData] = useState("");
//   const [children, setChildren] = useState([]);
//   const [isRunning, setIsRunning] = useState(true);
//   const [loading, setLoading] = useState(false);
//   const [click, setClick] = useState(false);
//   const [loadBeforeStrem, setShowBeforeStrem] = useState(true);
//   // const [checked, setChecked] = useState(false);
//   const snackbarRef = useRef(null);
//   //Datetime
//   const date = new Date();
//   const showTime =
//     date.getHours() + ":" + date.getMinutes() + ":" + date.getSeconds();

//   let flag = isRunning;
//   const start = -0.1;

//   const onLoadStart = (event) => {
//     event.preventDefault();

//     setLoading(true);
//     setClick(true);
//     /* Time taken by API to send data */
//     setTimeout(() => {
//       setLoading(false);
//       setShowBeforeStrem(false);
//     }, 1000);
//   };

//   const getDetection = async () => {
//     let flag = isRunning;
//     // const start = isToggled;
//     while (click && flag) {
//       console.log("before try isRunning,flag,start", isRunning, flag);
//       // console.log("in while buttonIsOn", buttonIsOn);
//       try {
//         const resp = await axios.get(urlDetaction);
//         //urlDetaction  = "http://127.0.0.1:8000/detection_percentage/"
//         console.log(resp);
//         let flag = resp.data.isRunning;
//         // console.log("in try buttonIsOn", buttonIsOn);
//         if (!isNaN(resp.data.det)) {
//           setData(resp.data.det);
//           // setData(start);
//           console.log("detection", resp.data.det);
//         }
//         if (flag === false) {
//           console.log("in flag start", flag);
//           break;
//         }
//       } catch (err) {
//         console.error(err);
//       }
//     }
//   };

//   useEffect(() => {
//     if (data > 0) {
//       setChildren((prev) => [
//         <div style={{ backgroundColor: getBackground(data) }}>
//           <h6>Detection:{data}</h6>
//           <h6> Cureent Time:{showTime}</h6>
//         </div>,
//         ...prev,
//       ]);
//     }
//   }, [data, showTime]);

//   useEffect(() => {
//     // console.log("buttonIsOn useeffect", buttonIsOn);
//     if (flag && click) {
//       getDetection();
//     }
//   }, [data, click]);

//   const getBackground = (data) => {
//     if (data > 0.01 && data <= 0.2) {
//       return "#fec9c9";
//     } else if (data > 0.2 && data <= 0.4) {
//       return "#ffa1a1";
//     } else if (data > 0.4 && data <= 0.6) {
//       return "#ff8080";
//     } else if (data > 0.6 && data <= 0.8) {
//       return "#ff5f5f";
//     } else if (data > 0.8 && data < 1) {
//       return "#ff0e0e";
//     }
//   };

//   return (
//     <div>
//       <div className={css.spiner}>
//         <LoadingSpinnerButton
//           title={"Load Data"}
//           loading={loading}
//           onClick={onLoadStart}
//         />
//       </div>
//       {click ? (
//         <img className={css.img} src={urlStream} alt="stream" />
//       ) : (
//         <div className={css.imgload}>
//           <SpinnerDiamond
//             style={{ marginLeft: 320, marginTop: 150 }}
//             size={150}
//             thickness={121}
//             speed={90}
//             color="rgba(110, 57, 172, 0.81)"
//             secondaryColor="rgba(57, 172, 154, 1)"
//           />
//         </div>
//       )}
//       {/* <ClipLoader
//           className={css.img}
//           loading={loadBeforeStrem}
//           size={150}
//           aria-label="Loading Spinner"
//           data-testid="loader"
//         /> */}
//       <div>
//         <div className={css.cat}>{children}</div>
//       </div>
//     </div>
//   );
// };

// export default Streamvideo;

// #All IMPORT
// import time
// import yolov5,torch
// import numpy as np
// import logging
// import pymongo
// import pickle
// import urllib
// import base64
// import gridfs
// import json
// import pafy
// import cv2
// import gridfs
// # import constant
// import sys
// import os
// import onnx
// import sys

// def index(request):
//     return render(request,'index.html')
// device = select_device('0') # 0 for gpu, '' for cpu

// print(torch.cuda.is_available())
// #load model
// # model = YOLO(path='C:/Users/ilaya/trainningModels/TREX2Base/best.pt')
// #model = torch.hub.load('ultralytics/yolov8', 'custom', path='C:/Users/ilaya/trainningModels/Rocket-Detect-27/best.pt',)
// #model = torch.hub.load('ultralytics/yolov5', 'yolov5s','yolov5s.onnx')
// #model = torch.hub.load('ultralytics/yolov5', 'custom',path='C:/Users/ilaya/trainningModels/TREX2FitWithin/best.pt',device=device)
// model = torch.hub.load('ultralytics/yolov5', 'custom',path='C:/Users/ilaya/trainningModels/pro/best.pt',device=device)
// #model = torch.hub.load('ultralytics/yolov','custom',path='C:/Users/ilaya/trainningModels/TREX2FitWithin/best.pt',device=device)

// # model = torch.hub.load('ultralytics/yolov5', 'custom',path='C:/Users/ilaya/trainningModels/TREX2Base/best.pt',device=device)
// #model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:/Users/ilaya/trainningModels/Rocket-Detect-32/300epmodel5n/best.pt',device=device)

// # initialize deepsort
// # cfg = get_config()
// # cfg.merge_from_file("deep_sort/configs/deep_sort.yaml")
// # deepsort = DeepSort('osnet_x0_25',
// #                     device,
// #                     max_dist=cfg.DEEPSORT.MAX_DIST,
// #                     max_iou_distance=cfg.DEEPSORT.MAX_IOU_DISTANCE,
// #                     max_age=cfg.DEEPSORT.MAX_AGE, n_init=cfg.DEEPSORT.N_INIT, nn_budget=cfg.DEEPSORT.NN_BUDGET,
// #                     )

// # Get names and colors

// names = model.module.names if hasattr(model, 'module') else model.names

// print("name",names)

// startvideo = False
// confidence = None
// check = True
// end=True
// det=0
// # global num_frames,elapsed_time,start_time
// # num_frames = 0
// # elapsed_time = 0
// # start_time = time.perf_counter()

// connect_str = "mongodb+srv://ilay:asis2003@cluster0.2mtny9z.mongodb.net/?retryWrites=true&w=majority"
// client = pymongo.MongoClient("mongodb+srv://ilay:asis2003@cluster0.2mtny9z.mongodb.net/?retryWrites=true&w=majority")
// connect = MongoClient(connect_str)

// def mongo_connection():
//     connect_str = "mongodb+srv://ilay:asis2003@cluster0.2mtny9z.mongodb.net/?retryWrites=true&w=majority"
//     try:
//         connect = MongoClient(connect_str)
//         print("Connect Succeed !",connect)
//         return connect.Rocket
//     except Exception as err:
//         print("Error connecting" + Exception)

// def stream(source):

//     end = False
//     detection_data = []
//     if startvideo :
//         global file_loc,file_name,fs,check,confidence,time_to_detect,det,previous_time_fps
//         time_to_detect = 0
//         path_to_frame = None
//         frame_counter = 0
//         source=content
//         locationvideo = content.split("/")
//         video_name=locationvideo[-1]
//         url = source + str('.mp4')
//         saveName = str('ResultOfVideo_') +str(video_name) + str('.mp4')
//         saveNameJson =  str('ResultOfVideo_') +str(video_name)
//         file_name=saveName
//         device = select_device('0')
//         path_to_save_video = "C:/Users/ilaya/LaunchVideos/VideoAfter/"
//         laoction_name = path_to_save_video + saveName
//         file_loc=laoction_name
//         cap = cv2.VideoCapture(url)
//         imageWidth = int(cap.get(3))
//         imageHeight = int(cap.get(4))
//         fps = cap.get(cv2.CAP_PROP_FPS)
//         #fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
//         # out = cv2.VideoWriter(laoction_name,fourcc,fps,(320, 320))
//         # cap.set(cv2.CAP_PROP_FPS, 120)
//         cap.set(cv2.CAP_PROP_FPS, 90)
//         cap.set(cv2.CAP_PROP_CONVERT_RGB, 1)
//         print("Source",source)
//         print("video_name",video_name)
//         print("url:",url)
//         print("laoction_name",laoction_name)
//         print("url",url)
//         path_uplode_video_withDetrction = (path_to_save_video) + (saveName)
//         model.conf=0.355
//         model.iou = 0.45
//         flagTime = True
//         while (cap.isOpened()):
//             if(flagTime):
//                 startS = time.time()
//                 flagTime = False
//             check = True
//             ret, frame = cap.read()
//             # time_to_detect_start = time.perf_counter()
//             start_time_fps = time.perf_counter()
//             if not ret:
//                 print("Error: failed to capture image")
//                 check = False
//                 print(str('Completed video ') + str(saveName))
//                 endE = time.time()
//                 break
//             frame = cv2.resize(frame, (320, 320))
//             frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
//             results = model(frame,augment=False,size=320)
//             end_time_fps = time.perf_counter()
//             fps = 1 / np.round(end_time_fps - start_time_fps, 3)
//             print("FPS :" , fps)
//             det = results.pred[0]
//             results.render()
//             # time_to_detect_end =  time.time()
//             # out.write(frame)
//             for *xyxy, conf, cls in det:
//                 floatNum=torch.IntTensor.item(conf)
//                 print("xyxy")
//                 num=f"{floatNum:.2f}"
//                 detection_conf = float(num)
//                 confidence = detection_conf
//                 path_to_frame =  "C:/Users/ilaya/LaunchVideos/Frame/BestFrameFor" +  str(saveName) + ".jpg"
//                 if confidence > 0.6:
//                     cv2.imwrite(path_to_frame,frame)
//                 x1 = int(xyxy[0].item())
//                 y1 = int(xyxy[1].item())
//                 x2 = int(xyxy[2].item())
//                 y2 = int(xyxy[3].item())
//                 width = x2 - x1
//                 height = y2 - y1
//                 surface_area = width * height
//                 time_to_detect=0
//                 #time_to_detect = time_to_detect_end -time_to_detect_start
//                 detection_data.append({
//                     "coordinates": [x1,y1,x2,y2],
//                     "confidence": confidence,
//                     "surface_area": surface_area,
//                     "time": time_to_detect
//                 })
//             annotator = Annotator(frame,line_width=2, pil=not ascii)
//             im0 = annotator.result()
//             image_bytes = cv2.imencode('.jpg', im0)[1].tobytes()

//             yield (b'--frame\r\n'
//                   b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n')

//         cap.release()
//         # out.release()

//         elapsed_time_ms = ( endE - startS )
//         print("time",elapsed_time_ms)
//         # print("frame_counter",frame_counter)
//         cv2.destroyAllWindows()
//         json_file_name = "detection_data_" + str(saveNameJson)+str(".json")
//         with open(json_file_name, "w") as f:
//             json.dump(detection_data, f)
//         end = True
//         print("json_file_name",json_file_name)
//         print("file_loc at end",file_loc,"filename",file_name)
//     if end:
//         upload_video_file_toMongo(file_loc=file_loc,file_name=file_name,json_file=json_file_name,path_to_frame=path_to_frame)
//         print("Done All")

// def upload_video_file_toMongo(file_loc,file_name,json_file,path_to_frame):
//     pathForUploadPhoto = path_to_frame
//     print("file loc at upload_video_file_toMongo",file_loc)
//     db = mongo_connection()
//     fs = gridfs.GridFS(db,collection="VideosDetection")

//     with open(file_loc,'rb') as file_data:
//         data = file_data.read()
//     with open(json_file, "r") as f:
//         json_data = json.load(f)
//     with open(pathForUploadPhoto, "rb") as f:
//         image_data = f.read()

//     metadata = {
//         "detectionData": json_data,
//         "image": image_data
//     }

//     #Check if a file with the same name already exists in the collection
//     existing_file = fs.find_one({"filename": file_name})

//     # Update the file if it already exists
//     if existing_file is not None:
//         # Delete the existing file
//         fs.delete(existing_file._id)
//         #Re-upload the file with the new data and metadata
//         fs.put(data, filename=file_name, metadata=metadata)
//         print("File updated successfully")
//     else:
//         # Add the new file to the collection
//         fs.put(data, filename=file_name, metadata=metadata)
//         print("File added successfully")

// def get_first_video_frame(path_to_frame,file_name,json_file):
//     fileNameToUpload=file_name
//     pathForUploadPhoto = path_to_frame
//     connect_str = "mongodb+srv://ilay:asis2003@cluster0.2mtny9z.mongodb.net/?retryWrites=true&w=majority"
//     client = pymongo.MongoClient(connect_str)
//     db = client["Rocket"]
//     fs = gridfs.GridFS(db,collection="VideosDetection")
//     with open(pathForUploadPhoto, "rb") as f:
//         image_data = f.read()
//     with open(json_file, "r") as f:
//         json_data = json.load(f)
//     file_id = fs.find_one({"filename": fileNameToUpload})._id
//     print("file id",file_id)
//     #put file into mongo DB
//     metadata = {
//         "detectionData": json_data,
//         "image": image_data
//     }
//     #metadata = db.fs.files.find_one({"_id": file_id}, {"metadata": 1})
//     # db.VideosDetection.files.update_one({"_id": file_id}, {"$set": {"metadata": metadata}})
//     update_metadata(file_id,metadata)
//     metadata = db.VideosDetection.files.find_one({"_id": file_id}, {"metadata": 1})
//     image_data = metadata["metadata"]["image"]
//     with open("image.jpg", "wb") as f:
//         f.write(image_data)
//     # Display the image using an image library such as Pillow
//     imageResult = im.open(BytesIO(image_data))
//     imageResult.show()

// def update_metadata(file_id, metadata):
//     # Connect to the MongoDB database
//     connect_str = "mongodb+srv://ilay:asis2003@cluster0.2mtny9z.mongodb.net/?retryWrites=true&w=majority"
//     client = pymongo.MongoClient(connect_str)
//     db = client["Rocket"]
//     fs = gridfs.GridFS(db, collection="VideosDetection")

//     # Update the metadata for the file with the given ID
//     try:
//         result = fs.VideosDetection.files.update_one(
//             {"_id": file_id},
//             {"$set": {"metadata": metadata}}
//         )
//         print("Metadata updated successfully")
//     except Exception as e:
//         print("Error updating metadata: ", e)

// def get_files(request):
//     # Connect to the MongoDB database
//     connect_str = "mongodb+srv://ilay:asis2003@cluster0.2mtny9z.mongodb.net/?retryWrites=true&w=majority"
//     client = pymongo.MongoClient(connect_str)
//     db = client["Rocket"]
//     fs = gridfs.GridFS(db,collection="VideosDetection")

//     # Find all the files in the database
//     files = fs.find()

//     data = []
//     # Iterate through the files and extract the metadata and filename
//     for file in files:
//         metadata = file.metadata
//         filename = file.filename

//         # Convert the binary data in the metadata to a base64-encoded string
//         if 'image' in metadata:
//             image_data = metadata['image']
//             metadata['image'] = base64.b64encode(image_data).decode('utf-8')

//         data.append({'filename': filename, 'metadata': metadata})

//     # Return the data as a JSON response
//     return HttpResponse(json.dumps(data), content_type='application/json')

// def detection():
//     while True:
//         if(not check):
//             data={"isRunning":False,"passtime":time_to_detect}
//             dataJson=json.dumps(data)
//             return dataJson
//         if(confidence is not None  and len(det) > 0):
//             data={"det":confidence,"isRunning":True,"passtime":time_to_detect}
//             dataJson=json.dumps(data)
//             return dataJson
//         data={"isRunning":True}
//         dataJson=json.dumps(data)
//         return dataJson
// @csrf_exempt
// def video_feed(request):
//     if request.method == 'POST':
//         global content
//         global start
//         content = request.GET.get('url','not')
//         print(content)
//     # video_thread = Thread(target=stream, args=(content,))
//     # detection_thread = Thread(target=detection)
//     # video_thread.start()
//     # detection_thread.start()
//     return StreamingHttpResponse(stream(content), content_type='multipart/x-mixed-replace; boundary=frame')

// def detection_percentage(request):
//     # video_thread = Thread(target=stream, args=(content,))
//     # detection_thread = Thread(target=detection)
//     # video_thread.start()
//     # detection_thread.start()
//     global startvideo
//     startvideo=True
//     return HttpResponse(detection())

// @csrf_exempt
// def load_video(request):
//     if request.method == 'GET':
//         #get the fileName
//         fileName = request.GET.get('filename','FailedGetFileName')
//         #connect to db
//         connect_str = "mongodb+srv://ilay:asis2003@cluster0.2mtny9z.mongodb.net/?retryWrites=true&w=majority"
//         client = pymongo.MongoClient(connect_str)
//         db = client["Rocket"]
//         fs = gridfs.GridFS(db,collection="VideosDetection")
//         #fine the spesific file
//         file = fs.find_one({"filename": fileName})
//         if file is None:
//             return HttpResponse(status=404)
//         print("i make a response with the video file" ,fileName )

//         response = HttpResponse()
//         response['Content-Type'] = 'application/json'

//         # read the file contents into a variable
//         file_contents = file.read()
//         # encode the binary data as a base64 string
//         file_contents_base64 = base64.b64encode(file_contents).decode('utf-8')

//         detection_data = fs.find_one({"filename": fileName}).metadata['detectionData']

//         # convert the detection data to a JSON-formatted string
//         detection_data_json = json.dumps(detection_data)
//         print("detection_data",detection_data_json)

//         # create a dictionary with the video and detection data
//         response_data = {'video': file_contents_base64, 'detectionData': detection_data_json}

//         # return the response as JSON
//         return HttpResponse(json.dumps(response_data), content_type='application/json')

{
  /* {/* <button
                class="btn btn-primary"
                onClick={() => {
                  // setToken(null);
                  // setUserName("");
                  // setAdmin(false);
                  localStorage.removeItem("user");
                  localStorage.removeItem("usename");
                  localStorage.removeItem("admin");
                  navigate("/session-timed-out");
                }}
              // > */
}
// Logout
// </button> */}
// const User = () => {
//   const [user, setUser] = useState();

//   const refreshToken = async () => {
//     const res = await axios
//       .get("http://localhost:5000/api/refresh", {
//         withCredentials: true,
//       })
//       .catch((err) => console.log(err));

//     const data = await res.data;
//     return data;
//   };

//   const sendRequest = async () => {
//     const res = await axios
//       .get("http://127.0.0.1:5000/api/user", {
//         withCredentials: true,
//       })
//       .catch((err) => console.log(err));
//     const data = res ? await res.data : null;
//     console.log("data", data);
//     return data;
//   };
//   useEffect(() => {
//     if (firstRender) {
//       firstRender = false;
//       sendRequest().then((data) => setUser(data.user));
//     }
//     let interval = setInterval(() => {
//       refreshToken().then((data) => setUser(data.user));
//     }, 1000 * 29);
//     return () => clearInterval(interval);
//   }, []);
//   return (
//     <div>
//       <div>
//         <h1>dssssssssc{user && user.name}</h1>
//         <h1></h1>
//       </div>
//     </div>
//   );
// };

// export default User;

// // const menuItems = [
//   const menuItems = [
//     {
//       name: "Verify",
//       to: `/`,
//       iconClassName: "bi bi-box-arrow-in-right",
//     },
//     {
//       name: "Add Users",
//       to: `/adduser`,
//       iconClassName: "bi bi-box-arrow-in-right",
//     },
//     {
//       name: "Log out",
//       to: `/`,
//       iconClassName: "bi bi-box-arrow-in-right",
//     },
//     {
//       name: "Live Stream",
//       to: "/live",
//       iconClassName: "bi bi-camera-video",
//     },
//     {
//       name: "Investigation Screen ",
//       to: `/investigation`,
//       iconClassName: "bi bi-display",
//     },
//     {
//       name: "Settings",
//       to: `/settings`,
//       iconClassName: "bi bi-gear",
//       // subMenus: [
//       //   { name: "Add new user", to: "/settings/adduser" },
//       //   { name: "Algoritam", to: "/settings/algoritam" },
//       //   { name: "Video url", to: "/settings/videourl" },
//       //   { name: "Frams", to: "/settings/frams" },
//       // ],
//     },
//   ];
