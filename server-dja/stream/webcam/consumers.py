import json
from channels.generic.websocket import AsyncWebsocketConsumer
import cv2
import asyncio
import base64
import datetime
import torch
from yolov5.utils.torch_utils import select_device
from django.conf import settings
import gridfs
from webcam.mongo import client

device = select_device('0')

model = torch.hub.load('ultralytics/yolov5', 'custom',path='C:/Users/ilaya/trainningModels/pro/new/best.pt',device=device)
#model = torch.hub.load("ultralytics/yolov5", 'custom', path='yolov5s.pt')
#model.classes = [0]  # Only person

import time
model=model.to(device)
model.iou = 0.49
model.conf = 0.35
class StreamConsumer(AsyncWebsocketConsumer):
    url_received = False
    start_received = False
    active_received= False

    url = None
    start = None
    active = None
    
    async def connect(self):
        await self.accept()     

    async def receive(self, text_data):
        print("hi from receive")
        text_data_json = json.loads(text_data)
        print(text_data_json)
        if 'url' in text_data_json:
            self.url = text_data_json['url']
            StreamConsumer.url_received = self.url_received = True
            StreamConsumer.url = self.url
            print("hi from receive url")
        if 'active' in text_data_json:
            self.active = text_data_json['active']
            StreamConsumer.active_received = self.active_received = True
            StreamConsumer.active = self.active
              
        if StreamConsumer.url_received and StreamConsumer.active_received :
             await self.send(json.dumps({'message': "Received Url and Active successfully!"}))
        if StreamConsumer.url_received is False or StreamConsumer.active_received is False :
            await self.send(json.dumps({'message': "Didnt Received Url or Active !"}))
        if 'start' in text_data_json:
            self.start = text_data_json['start']
            StreamConsumer.start_received = self.start_received = True
            StreamConsumer.start = self.start
            print("hi from receive start",self.start)
       
        print("before if ",self.start_received ,self.url_received,self.active_received)
        if StreamConsumer.url_received and StreamConsumer.start_received and StreamConsumer.active_received :
            
            print("hi from receive go",self.url,self.start)
            await self.send_frames(self.url, self.start,self.active)
            StreamConsumer.url_received = self.url_received = False
            StreamConsumer.start_received = self.start_received = False  
            StreamConsumer.activeAlgorithm = self.activeAlgorithm = False
         

    async def send_frames(self,urlvideo,canToStart,IsActive):
        stream_on = False
        IsActive = IsActive
        #set camera 
        print("IsActive Insdie :",IsActive)
        self.camera = cv2.VideoCapture(urlvideo +str('.mp4'))
        sizeFrame=320
        #set details about video
        self.fps = self.camera.get(cv2.CAP_PROP_FPS)
        image_width = int(self.camera.get(3))
        image_height = int(self.camera.get(4))
        #saving frame and video
        locationvideo = urlvideo.split("/")
        video_name=locationvideo[-1]
        saveName = str('ResultOfVideo_') +str(video_name) + str('.mp4')
        saveNameFrame = str(video_name)
        json_file_name = "detection_data_" + str('ResultOfVideo_') +str(video_name)+str(".json")
        path_to_frame = "C:/Users/ilaya/LaunchVideos/Frame/BestFrameFor" + saveNameFrame + ".jpg"
        #details saving about the video
        path_to_save_video =  "C:/Users/ilaya/LaunchVideos/VideoAfter/" + saveName
        fps = self.camera.get(cv2.CAP_PROP_FPS)
        fourcc = cv2.VideoWriter_fourcc(*'VIDX')
        out = cv2.VideoWriter(path_to_save_video,fourcc,fps,
                              (sizeFrame, sizeFrame))
        #details saving about the video
        current_frame = 1
        print("fps",fps)
        frame_count = int(self.camera.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = frame_count / fps
        #definitions
        startAll = time.time()
        max_confidence = 0
        detection_data = []
        while True:
            stream_on = True
            ret, frame = self.camera.read()
            if not ret:
                endAll = time.time()
                print("Length of time between first frame and last frame: ", duration )
                end_All_video = ( endAll - startAll ) 
                print("actually time takse : ",end_All_video, " seconds.")
                stream_on = False
                break
            if ret:
                frame = cv2.resize(frame, (sizeFrame, sizeFrame))
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                results = model(frame, augment=False, size=sizeFrame)
                if(IsActive):
                    results.render()
                out.write(frame)
                _, buffer = cv2.imencode('.jpg', frame)
                encoded_frame = base64.b64encode(buffer).decode()
                labels, cord = results.xyxyn[0][:, -1].cpu().numpy(), results.xyxyn[0][:, :-1].cpu().numpy()
                n = len(labels)
                confidence = 0
                for i in range(n):
                    # crops = results.crop(save=True)
                    current_time = current_frame / fps
                    current_time = round(current_time, 4)
                    xmin, ymin, xmax, ymax, confidenceObject = cord[0][0], cord[0][1], cord[0][2], cord[0][3], cord[0][4]
                    print("before",xmin, ymin, xmax, ymax, confidenceObject)
                    width = int((xmax - xmin) * sizeFrame)
                    height = int((ymax - ymin) * sizeFrame)
                    surface_area = width * height
                    #pascal_voc
                    xmin = int(round(xmin, 4) * sizeFrame)
                    ymin = int(round(ymin, 4) * sizeFrame)
                    xmax = int(round(xmax, 4) * sizeFrame)
                    ymax = int(round(ymax, 4) * sizeFrame)
                    confidenceObject = round(confidenceObject, 2)
                    print(xmin, ymin, xmax, ymax, confidenceObject)
                   
                    # calculate the width and height of the bounding box in pixels
                    detection_data.append({
                        "coordinates": str([xmin, ymin, xmax, ymax]),
                        "xmin":str(xmin),
                        "ymin":str(ymin),
                        "xmax":str(xmax),
                        "ymax":str(ymax),
                        "confidence": str(confidenceObject),
                        "surface_area": str(surface_area),
                        "time": current_time
                    })
                    
                    print("surface_area",surface_area)
                    print("cord ",xmin, ymin, xmax, ymax,confidenceObject)
                    confidence = f"{confidenceObject:.2f}"
                    if confidenceObject > max_confidence:
                        max_confidence = confidenceObject   
                        cv2.imwrite(path_to_frame, frame)
                current_time = current_frame / fps
                print("current_time",current_time)
                current_frame += 1
                print("current_frame",current_frame)
                if(IsActive):
                    await self.send(json.dumps({"streamOn":stream_on,'frame': encoded_frame, "time": current_time, "confidence": str(confidence)}))
                else:
                    await self.send(json.dumps({"streamOn":stream_on,'frame': encoded_frame, "time": current_time}))
            await asyncio.sleep(0.001)

        print("Done")
        if(IsActive):
            with open(json_file_name, "w") as f:
                json.dump(detection_data, f)
        
        self.camera.release()
        out.release()
        cv2.destroyAllWindows()
        if(IsActive):
            await self.send(json.dumps({"streamOn":stream_on}))
            await self.upload_video_file_toMongo(path_to_save_video,saveName,json_file_name,path_to_frame)


    async def upload_video_file_toMongo(self,path_to_save_video,saveName,json_file_name,path_to_frame):
        now = datetime.datetime.now()
        formatted_date_time = now.strftime("%Y-%m-%d / %H:%M")
        #connect to mongo DB
        print("file_loc ",path_to_save_video," file_name : ",saveName," json_file : ",json_file_name," path_to_frame :",path_to_frame)
        db = client[settings.DATABASES['default']['NAME']]
        # collection = db['VideosDetection']    
        # connect_str = settings.DATABASES['default']['CLIENT']['host']
        # print("connect_str",connect_str)
        # connect = MongoClient(connect_str)
        # print("connect",connect)
        # db = connect.get_database(settings.DATABASES['default']['NAME'])
        print("db",db)
        fs = gridfs.GridFS(db, collection="VideosDetection")
        print("fs",fs)

        #uploud file with all data to db
        with open(path_to_save_video,'rb') as file_data:
            data = file_data.read()
        with open(json_file_name, "r") as f:
            json_data = json.load(f)    
        with open(path_to_frame, "rb") as f:
            image_data = f.read()

        metadata = {
            "Data": json_data,
            "Image": image_data,
            "Date":formatted_date_time,
        }

        #Check if a file with the same name already exists in the collection
        existing_file = fs.find_one({"filename": saveName})

        # Update the file if it already exists
        if existing_file is not None:
            # Delete the existing file
            fs.delete(existing_file._id)
            #Re-upload the file with the new data and metadata
            fs.put(data, filename=saveName, metadata=metadata)
            print("File updated successfully")
        else:
            # Add the new file to the collection
            fs.put(data, filename=saveName, metadata=metadata)
            print("File added successfully")



   
   
#model = torch.hub.load('ultralytics/yolov5', 'custom',path='C:/Users/ilaya/trainningModels/pro/best.pt',device=device)
#model = torch.hub.load('ultralytics/yolov5', 'custom',path='C:/Users/ilaya/trainningModels/MoreEp/best.pt',device=device)

    # async def disconnect(self, close_code):
    #     # raise StopConsumer()
    #     # self.camera.release()





# import cv2

# # Load video file
# cap = cv2.VideoCapture("path/to/video/file.mp4")

# # Object dimensions in cm
# object_width_cm = 10
# focal_length_pixels = 1000
# sensor_width_pixels = 5000

# # Calculate conversion factor
# conversion_factor_cm_per_pixel = (object_width_cm * focal_length_pixels) / sensor_width_pixels

# # Load YOLO model
# # ...

# while True:
#     # Read a frame from the video
#     ret, frame = cap.read()
#     if not ret:
#         break
    
#     # Run YOLO on the frame
#     # ...
    
#     # Process YOLO results
#     for cord in cords:
#         xmin, ymin, xmax, ymax = cord[0], cord[1], cord[2], cord[3]
        
#         # Convert pixel dimensions to cm dimensions
#         xmin_cm = xmin * conversion_factor_cm_per_pixel
#         ymin_cm = ymin * conversion_factor_cm_per_pixel
#         xmax_cm = xmax * conversion_factor_cm_per_pixel
#         ymax_cm = ymax * conversion_factor_cm_per_pixel
#         width_cm = (xmax - xmin) * conversion_factor_cm_per_pixel
#         height_cm = (ymax - ymin) * conversion_factor_cm_per_pixel
        
#         # Calculate surface area in cm²
#         surface_area_cm_squared = 2 * (width_cm * height_cm + width_cm * object_width_cm + height_cm * object_width_cm)























