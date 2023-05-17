import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import classes from "../../css/admin/Settings.module.css";
import LibraryAddCheckIcon from "@mui/icons-material/LibraryAddCheck";
import Button from "@mui/material/Button";
// import * as React from "react";
import TextField from "@mui/material/TextField";
import Autocomplete from "@mui/material/Autocomplete";
import SaveIcon from "@mui/icons-material/Save";
// "https://www.youtube.com/watch?v=2GD5hW8bMFQ&list=LL&index=56",
//"https://www.youtube.com/watch?v=St1lbeBkTkc",
//"https://www.youtube.com/watch?v=yRK_AqSeHLQ",

const options = [
  "C:/Users/ilaya/LaunchVideos/VideoBefore/MissileLaunch1",
  "C:/Users/ilaya/LaunchVideos/VideoBefore/MissileLaunch2",
  "C:/Users/ilaya/LaunchVideos/VideoBefore/MissileLaunch3",
  "C:/Users/ilaya/LaunchVideos/VideoBefore/MissileLaunch4",
  "C:/Users/ilaya/LaunchVideos/VideoBefore/MissileLaunch5",
];

const Settings = () => {
  const [value, setValue] = useState(options[0]);
  const [inputValue, setInputValue] = useState("");
  const navigate = useNavigate();

  // const ws = new WebSocket("ws://localhost:8000/ws/stream/");

  // let socket;
  let socket;
  const onClick = () => {
    socket = new WebSocket("ws://localhost:8000/ws/stream/");
    socket.onopen = function (event) {
      socket.send(
        JSON.stringify({
          url: inputValue,
        })
      );
      navigate("/live");
    };
  };

  return (
    <section className={classes.auth}>
      <div>
        {/* <div>{`value: ${value !== null ? `'${value}'` : "null"}`}</div>
        <div>{`inputValue: '${inputValue}'`}</div> */}
        {/* <br /> */}
        <div>
          <h1 className={classes.h1}>Settings page</h1>
        </div>
        <div>
          <h4 className={classes.h4}>Enter Url For Streming Video</h4>
          <Autocomplete
            value={value}
            onChange={(event, newValue) => {
              setValue(newValue);
            }}
            inputValue={inputValue}
            onInputChange={(event, newInputValue) => {
              setInputValue(newInputValue);
            }}
            id="controllable-states-demo"
            options={options}
            sx={{ width: 300 }}
            renderInput={(params) => (
              <TextField {...params} label=" Stream URL" />
            )}
          />
          <div className={classes.confirmButton}>
            <Button
              variant="contained"
              onClick={onClick}
              startIcon={<LibraryAddCheckIcon />}
            >
              Set Url
            </Button>
          </div>
          <div className={classes.saveButton}>
            <Button variant="contained" startIcon={<SaveIcon />}>
              Save URL
            </Button>
          </div>
        </div>
      </div>
    </section>
  );
};
export default Settings;

// # startvideo =False
// # confidence = None
// # check = True
// # end=True
// # time_to_detect=0
// # det=0
// # start =  timer.time()

// # def stream(source):
// #     if startvideo :
// #         saveName = str('ResultOfVideo_') + str(source) + str('.avi')
// #         source=content
// #         urlPafy = pafy.new(source)
// #         videoplay = urlPafy.getbest(preftype="any")
// #         if source.startswith(("C:",'Users','ilaya')):
// #             url = source + str('.mp4')
// #             cap = cv2.VideoCapture(url)

// #         # elif source.startswith(("http",'youtu','www')):
// #         #    url_data = urllib.parse.urlparse(source)
// #         #    query = urllib.parse.parse_qs(url_data.query)
// #         #    id = query["v"][0]
// #         #    video = 'https://youtu.be/{}'.format(str(id))
// #         #
// #         print("Source",source)
// #         cap = cv2.VideoCapture(videoplay.url)
// #         imageWidth = int(cap.get(3))
// #         imageHeight = int(cap.get(4))
// #         model.conf=0.15
// #         fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
// #         #fps = cap.get(cv2.CAP_PROP_FPS)
// #         # out = cv2.VideoWriter(saveName,fourcc, 8.0,(imageWidth, imageHeight))
// #         #out = cv2.VideoWriter('output.avi',fourcc, 20.0,(int(cap.get(3)),int(cap.get(4))))
// #         #model.iou=0.5
// #         global check
// #         global confidence
// #         global time_to_detect
// #         global det
// #         while (cap.isOpened()):
// #             ret, frame = cap.read()
// #             print("source",source)
// #             check = True
// #             if not ret:
// #                 print("Error: failed to capture image")
// #                 check = False
// #                  # print(str('Completed video ') + str(saveName))
// #                 break
// #             results = model(frame,augment=False,size=640)
// #             # frame= cv2.resize(frame,(1200,700))
// #             det = results.pred[0]
// #             results.render()
// #             for *xyxy, conf, cls in det:
// #                 floatNum=torch.IntTensor.item(conf)
// #                 num=f"{floatNum:.2f}"
// #                 detection_conf = float(num)
// #                 confidence = detection_conf
// #                 end = timer.time()
// #                 time_to_detect = end-start
// #             annotator = Annotator(frame, line_width=2, pil=not ascii)
// #             im0 = annotator.result()
// #             image_bytes = cv2.imencode('.jpg', im0)[1].tobytes()
// #             yield (b'--frame\r\n'
// #                    b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n')
// #          # out.write(frame)
// #         cap.release()
// #         # out.release()
// #         cv2.destroyAllWindows()

// # def detection():
// #     while True:
// #         if(not check):
// #             data={"isRunning":False,"passtime":time_to_detect}
// #             dataJson=json.dumps(data)
// #             return dataJson
// #         if(confidence is not None  and len(det) > 0):
// #             data={"det":confidence,"isRunning":True,"passtime":time_to_detect}
// #             dataJson=json.dumps(data)
// #             return dataJson
// #         data={"isRunning":True}
// #         dataJson=json.dumps(data)
// #         return dataJson

// # def detections_data():
// #     end = True
// #     if(confidence is not None  and len(det) > 0):
// #         final_json=[{"detection":confidence,"passtime":time_to_detect}]
// #         dataJsonFinal=json.dumps(final_json)
// #     if end is False:
// #         return dataJsonFinal

// # def video_id(url):
// #     if url.startswith(('youtu','www')):
// #         url = 'http://' + url
// #     query = urlparse(url)
// #     if 'youtube' in query.hostname:
// #         if query.path == '/watch':
// #             return parse_qs(query.query)['v'][0]
// #         elif query.path.startswith(('/embed','/v/')):
// #             return query.path.split('/')[2]
// #     elif 'youtube.be' in query.hostname:
// #         return query.path[1:]
// #     else:
// #         raise ValueError

// # @csrf_exempt
// # def video_feed(request):
// #     if request.method == 'POST':
// #         global content
// #         global youtubeUrl
// #         global start
// #         url = request.GET.get('url','not')
// #         if url.startswith("http"):
// #             youtubeUrl = url
// #             content=youtube_url(youtubeUrl)
// #         elif url.startswith(("C:",'Users','ilaya')):
// #             content = url
// #         print(content)
// #     return StreamingHttpResponse(stream(content), content_type='multipart/x-mixed-replace; boundary=frame')

// # def detection_percentage(request):
// #     global startvideo
// #     startvideo = True
// #     return HttpResponse(detection())

// # def data(request):
// #     return HttpResponse(detections_data())
