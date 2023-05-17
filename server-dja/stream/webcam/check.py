# from fastapi import FastAPI
# from fastapi.websockets import WebSocket
# from fastapi.responses import HTMLResponse

# app=FastAPI()


# @app.websocket("/ws/")
# async def websocket_handler(websocket: WebSocket):
#         await websocket.accept()
#         print("Accepted connection")
#         while True:
#             try:
#                 data = await websocket.receive_text()
#                 await websocket.send_text("send from server")
#                 print("Success")
#             except:
#                 break
#         await websocket.close()



# def get_first_video_frame(path_to_frame,file_name,json_file):
#     fileNameToUpload=file_name
#     pathForUploadPhoto = path_to_frame
#     connect_str = "mongodb+srv://ilay:asis2003@cluster0.2mtny9z.mongodb.net/?retryWrites=true&w=majority"
#     client = pymongo.MongoClient(connect_str)
#     db = client["Rocket"]
#     fs = gridfs.GridFS(db,collection="VideosDetection")
#     with open(pathForUploadPhoto, "rb") as f:
#         image_data = f.read()
#     with open(json_file, "r") as f:
#         json_data = json.load(f)    
#     file_id = fs.find_one({"filename": fileNameToUpload})._id
#     print("file id",file_id)
#     #put file into mongo DB
#     metadata = {
#         "Data": json_data,
#         "Image": image_data
#     }
#     #metadata = db.fs.files.find_one({"_id": file_id}, {"metadata": 1})
#     # db.VideosDetection.files.update_one({"_id": file_id}, {"$set": {"metadata": metadata}})
#     update_metadata(file_id,metadata)
#     metadata = db.VideosDetection.files.find_one({"_id": file_id}, {"metadata": 1})
#     image_data = metadata["metadata"]["Image"]
#     with open("image.jpg", "wb") as f:
#         f.write(image_data)
#     # Display the image using an image library such as Pillow
#     imageResult = im.open(BytesIO(image_data))
#     imageResult.show()

# class DetectionData(View):
#     def get(self, request):
#         context = {
#             'confidence':confidence
#         }
#         # return render(request,'detection/index.html',context)



# def detection_percentage(request):
#     # video_thread = Thread(target=stream, args=(content,))
#     # detection_thread = Thread(target=detection)
#     # video_thread.start()
#     # detection_thread.start()
#     global startvideo
#     startvideo=True
#     return HttpResponse(detection())




# def stream2(source):
#     end = False
#     detection_data = []
#     if startvideo : 
#         global file_loc,file_name,fs,check,confidence,time_to_detect,det,previous_time_fps
#         time_to_detect = 0
#         path_to_frame = None
#         source=content
#         locationvideo = content.split("/")
#         video_name=locationvideo[-1]
#         url = source + str('.mp4')
#         saveName = str('ResultOfVideo_') +str(video_name) + str('.mp4')
#         saveNameJson =  str('ResultOfVideo_') +str(video_name)
#         file_name=saveName
#         path_to_save_video = "C:/Users/ilaya/LaunchVideos/VideoAfter/"
#         laoction_name = path_to_save_video + saveName
#         file_loc=laoction_name
#         cap = cv2.VideoCapture(url)
#         imageWidth = int(cap.get(3))
#         imageHeight = int(cap.get(4))
#         fps = cap.get(cv2.CAP_PROP_FPS)
#         #fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
#         # out = cv2.VideoWriter(laoction_name,fourcc,fps,(320, 320))
#         # cap.set(cv2.CAP_PROP_FPS, 120)
#         cap.set(cv2.CAP_PROP_FPS, 30) 
#         cap.set(cv2.CAP_PROP_CONVERT_RGB, 1)
#         print("Source",source)
#         print("video_name",video_name)
#         print("url:",url)
#         print("laoction_name",laoction_name)
#         path_uplode_video_withDetrction = (path_to_save_video) + (saveName)
#         # model.conf=0.355
#         # model.iou = 0.45
#         flagTime = True
#         channel_layer = get_channel_layer()
#         while (cap.isOpened()):
#             if(flagTime):
#                 startS = time.time()
#                 flagTime = False
#             check = True
#             ret, frame = cap.read()
#             # time_to_detect_start = time.perf_counter()
#             start_time_fps = time.perf_counter()
#             if not ret:
#                 print("Error: failed to capture image")
#                 check = False
#                 print(str('Completed video ') + str(saveName))
#                 endE = time.time()
#                 break
#             frame = cv2.resize(frame, (320, 320))
#             #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#             results = model(frame,augment=False,size=320)
#             end_time_fps = time.perf_counter()
#             fps = 1 / np.round(end_time_fps - start_time_fps, 3)
#             print("FPS :" , fps)
#             det = results.pred[0]
#             results.render()
#             # time_to_detect_end =  time.time()
#             # out.write(frame)   
#             for *xyxy, conf, cls in det:
#                 floatNum=torch.IntTensor.item(conf)
#                 print("xyxy")
#                 num=f"{floatNum:.2f}"
#                 detection_conf = float(num)
#                 confidence = detection_conf
#                 path_to_frame =  "C:/Users/ilaya/LaunchVideos/Frame/BestFrameFor" +  str(saveName) + ".jpg"
#                 if confidence > 0.6:
#                     cv2.imwrite(path_to_frame,frame)
#                 x1 = int(xyxy[0].item())
#                 y1 = int(xyxy[1].item())
#                 x2 = int(xyxy[2].item())
#                 y2 = int(xyxy[3].item())
#                 width = x2 - x1
#                 height = y2 - y1
#                 surface_area = width * height
#                 time_to_detect=0
#                 #time_to_detect = time_to_detect_end -time_to_detect_start 
#                 detection_data.append({
#                     "coordinates": [x1,y1,x2,y2],
#                     "confidence": confidence,
#                     "surface_area": surface_area,
#                     "time": time_to_detect
#                 })
#             annotator = Annotator(frame,line_width=2, pil=not ascii)
#             im0 = annotator.result()
#             image_bytes = cv2.imencode('.jpg', im0)[1].tobytes()
            
#             yield (b'--frame\r\n'
#                   b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n')

#         cap.release()
#         # out.release()
        
#         elapsed_time_ms = ( endE - startS ) 
#         print("time",elapsed_time_ms)
#         # print("frame_counter",frame_counter)
#         cv2.destroyAllWindows()
#         json_file_name = "detection_data_" + str(saveNameJson)+str(".json")
#         with open(json_file_name, "w") as f:
#             json.dump(detection_data, f)
#         end = True
#         print("json_file_name",json_file_name)
#         print("file_loc at end",file_loc,"filename",file_name)
#     if end:
#         upload_video_file_toMongo(file_loc=file_loc,file_name=file_name,json_file=json_file_name,path_to_frame=path_to_frame)
#         print("Done All")







# def stream4(source):
#         end = False
#         detection_data = []
#         global file_loc,file_name,fs,check,confidence,time_to_detect,det,previous_time_fps
#         time_to_detect = 0
#         path_to_frame = None
#         source=content
#         locationvideo = content.split("/")
#         video_name=locationvideo[-1]
#         url = source + str('.mp4')

#         saveName = str('ResultOfVideo_') +str(video_name) + str('.mp4')
#         saveNameJson =  str('ResultOfVideo_') +str(video_name)
#         file_name=saveName
#         path_to_save_video = "C:/Users/ilaya/LaunchVideos/VideoAfter/"
#         laoction_name = path_to_save_video + saveName
#         file_loc=laoction_name

#         cap = cv2.VideoCapture("C:/Users/ilaya/LaunchVideos/VideoBefore/MissileLaunch3.mp4")
#         imageWidth = int(cap.get(3))
#         imageHeight = int(cap.get(4))
#         fps = cap.get(cv2.CAP_PROP_FPS)
#         fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
#         out = cv2.VideoWriter(laoction_name,fourcc,fps,(320, 320))
#         # cap.set(cv2.CAP_PROP_FPS, 120)
#         cap.set(cv2.CAP_PROP_FPS, 120) 
#         cap.set(cv2.CAP_PROP_CONVERT_RGB, 1)
#         print("Source",source)
#         print("video_name",video_name)
#         print("url:",url)
#         print("laoction_name",laoction_name)
#         print("url",url)
#         path_uplode_video_withDetrction = (path_to_save_video) + (saveName)
#         # model.conf=0.355
#         # model.iou = 0.45
#         flagTime = True
#         while (cap.isOpened()):
#             print("i am inside")
#             if(flagTime):
#                 startS = time.time()
#                 flagTime = False
#             check = True
#             ret, frame = cap.read()
#             # time_to_detect_start = time.perf_counter()
#             start_time_fps = time.perf_counter()
#             if not ret:
#                 print("Error: failed to capture image")
#                 check = False
#                 print(str('Completed video ') + str(saveName))
#                 endE = time.time()
#                 break
#             frame = cv2.resize(frame, (320, 320))
#             frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#             results = model(frame,augment=False,size=320)
#             end_time_fps = time.perf_counter()
#             fps = 1 / np.round(end_time_fps - start_time_fps, 3)
#             print("FPS :" , fps)
#             det = results.pred[0]
#             results.render()
#             # time_to_detect_end =  time.time()
#             # out.write(frame)   
#             for *xyxy, conf, cls in det:
#                 floatNum=torch.IntTensor.item(conf)
#                 print("xyxy")
#                 num=f"{floatNum:.2f}"
#                 detection_conf = float(num)
#                 confidence = detection_conf
#                 path_to_frame =  "C:/Users/ilaya/LaunchVideos/Frame/BestFrameFor" +  str(saveName) + ".jpg"
#                 if confidence > 0.6:
#                     cv2.imwrite(path_to_frame,frame)
#                 x1 = int(xyxy[0].item())
#                 y1 = int(xyxy[1].item())
#                 x2 = int(xyxy[2].item())
#                 y2 = int(xyxy[3].item())
#                 width = x2 - x1
#                 height = y2 - y1
#                 surface_area = width * height
#                 time_to_detect=0
#                 #time_to_detect = time_to_detect_end -time_to_detect_start 
#                 detection_data.append({
#                     "coordinates": [x1,y1,x2,y2],
#                     "confidence": confidence,
#                     "surface_area": surface_area,
#                     "time": time_to_detect
#                 })
#             annotator = Annotator(frame,line_width=2, pil=not ascii)
#             im0 = annotator.result()
#             image_bytes = cv2.imencode('.jpg', im0)[1].tobytes()
#             yield (b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n')
#         cap.release()
#         # out.release()
#         elapsed_time_ms = ( endE - startS ) 
#         print("time",elapsed_time_ms)
#         # print("frame_counter",frame_counter)
#         cv2.destroyAllWindows()
#         json_file_name = "detection_data_" + str(saveNameJson)+str(".json")
#         with open(json_file_name, "w") as f:
#             json.dump(detection_data, f)
#         end = True
#         print("json_file_name",json_file_name)
#         print("file_loc at end",file_loc,"filename",file_name)
#         # if end:
#         #     upload_video_file_toMongo(file_loc=file_loc,file_name=file_name,json_file=json_file_name,path_to_frame=path_to_frame)
#         #     print("Done All")







# from asgiref.sync import async_to_sync
# import json
# from channels.generic.websocket import AsyncWebsocketConsumer
# import cv2
# import json
# from django.http import JsonResponse
# from asgiref.sync import async_to_sync
# from asgiref.sync import async_to_sync
# from channels.generic.websocket import AsyncWebsocketConsumer
# import asyncio
# import base64
# import torch
# from yolov5.utils.plots import Annotator
# from yolov5.utils.torch_utils import select_device
# device = select_device('0')
# model = torch.hub.load('ultralytics/yolov5', 'custom',path='C:/Users/ilaya/trainningModels/pro/best.pt',device=device)
# import time
# class StreamConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         await self.accept()
#     async def receive(self,text_data):
#         text_data_json = json.loads(text_data)
#         if text_data_json['type'] == 'url':
#             url = text_data_json['url']
#             self.camera = cv2.VideoCapture(url)
#         # await self.accept()
#         # url = "C:/Users/ilaya/LaunchVideos/VideoBefore/MissileLaunch3.mp4"
#         # self.camera = cv2.VideoCapture(url)
#             self.camera.set(cv2.CAP_PROP_CONVERT_RGB, 1)
#             while True:

#                 start_time = time.perf_counter()
#                 async def send_frames():
#                     self.camera.set(cv2.CAP_PROP_FPS, 90)
#                     start_time_fps = time.time()
#                     frame_count = 0
#                     while True:
#                         model.iou = 0.45 
#                         model.conf = 0.35
#                         ret, frame = self.camera.read()
#                         if not ret:
#                             end_time = time.perf_counter()
#                             print("Length of time between first frame and last frame: ", end_time - start_time)
#                             break
#                 # startTime = time.time()
#                         if ret:
#                             frame = cv2.resize(frame, (320, 320))
#                             frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#                             results = model(frame,augment=False,size=320)
#                             results.render()
#                             _, buffer = cv2.imencode('.jpg', frame)
#                             encoded_frame = base64.b64encode(buffer).decode()
#                             labels, cord = results.xyxyn[0][:, -1].cpu().numpy(), results.xyxyn[0][:, :-1].cpu().numpy()
#                             n = len(labels)
#                             confidence = 0
#                             for i in range(n):
#                                 row = cord[i]
#                                 confidenceFloat=row[4]
#                                 confidence=f"{confidenceFloat:.2f}"
#                                 print("confidence : ",confidence)                       
#                                 # frame_count += 1
#                                 # elapsed_time_fps= time.time() - start_time_fps
#                                 # fps = frame_count / elapsed_time_fps
#                                 # print("FPS:",fps)
#                             # frame_count += 1
#                             # elapsed_time_fps= time.time() - start_time_fps
#                             # fps = frame_count / elapsed_time_fps
#                             # print("FPS:",fps)
#                         await self.send(json.dumps({'frame': encoded_frame,"confidence":str(confidence)}))
#                     await asyncio.sleep(0)
#                 await send_frames()
                
#     async def disconnect(self, close_code):    
#         self.camera.release()

# annotator = Annotator(frame,line_width=2, pil=not ascii)
# im0 = annotator.result()
# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.room_group_name = 'test'
#         await self.channel_layer.group_add(
#             self.room_group_name,
#             self.channel_name
#         )
#         await self.accept()

#     async def receive(self,text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']

#         await self.channel_layer.group_send(
#             self.room_group_name, {
#                 'type':'chat_message',
#                 'message':message
#             }
#         )

#     async def chat_message(self,event):
#         message = event['message']

#         await self.send(text_data=json.dumps({
#             'type':'chat',
#             'message':message
#         }))


# class ChatConsumer(AsyncWebsocketConsumer):
#     def connect(self):
#         self.room_group_name = 'test'
#         async_to_sync(self.channel_layer.group_add)(
#             self.room_group_name,
#             self.channel_name
#         )
#         self.accept()

       

#     def receive(self,text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']
        
        
#         async_to_sync(self.channel_layer.group_send)(
#             self.room_group_name, {
#                 'type':'chat_message',
#                 'message':message
#             }
#         )

#     def chat_message(self,event):
#         message = event['message']

#         self.send(text_data=json.dumps({
#             'type':'chat',
#             'message':message
#         }))



         # self.send(text_data=json.dumps({
        #     'type':'connection_established',
        #     'message':'you are connect'
        # }))

        # self.send(text_data=json.dumps({
        #     'type': 'chat',
        #     'message':message
        # }))

# class DetectionConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         await self.accept()

#     async def disconnect(self, close_code):
#         pass

#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']
#         confidence = text_data_json['confidence']

#         # Do something with the message and confidence here
#         # You could for example send it to another part of your application for processing

#         await self.send(text_data=json.dumps({
#             'message': message,
#             'confidence': confidence
#         }))



# class DetectionConsumer(AsyncWebsocketConsumer):
#     async def websocket_connect(self,event):
#         detections_room = 'detection'
#         self.detections_message = detections_room
#         await self.channel_layer.group_add(
#             detections_room,self.channel_name
#         )
#         await self.send({
#             "type":"websocket.accept"
#         })
   

#     #Resive message from websocket
#     async def websocket_receive(self, event):
#         inital_data=event.get("text",None)
#         await self.channel_layer.group_send(
#             self.detections_room,{
#                 "type" : "detections_message",
#                 "text" : inital_data
#             }
#         )
    
#     async def websocket_message(self, event):
#         await self.send({
#             "type":"websocket.send",
#             "text" :"hi"
#         })

#     async def websocket_disconnect(self,event):
#        print("disconnect from socket happend",event)


#     # confidence = event["confidence"]

#     # #send message to websocket
#     # await self.send(text_data=json.dumps({"confidence": confidence}))
#     #recive message from group
  
    
# # from asgiref.sync import async_to_sync
# # from .views import stream
#     # async def send(self, event):
#     #     confidence = event["confidence"]
#     #     await self.send(text_data=json.dumps({"confidence": confidence}))
    

#     # async def start_stream(self, source):
#     #     async_to_sync(self.channel_layer.group_add)("detection_group", self.channel_name)
#     #     stream(source, self.channel_layer, self.channel_name)

#      # # text_data_json = json.loads(text_data)
#         # # confidence = text_data_json['confidence']

#         # # event = {
#         # #     'type' : 'send_message',
#         # #     'confidence' : confidence
#         # # }

#         # # send message to group
#         # await self.channel_layer.group_send(self.group_name,event)



