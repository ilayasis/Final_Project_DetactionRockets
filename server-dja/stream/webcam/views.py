#All FORM
from yolov5.utils.general import (check_img_size, non_max_suppression, scale_coords, 
                                  check_imshow, xyxy2xywh, increment_path)
from django.http import HttpResponse
from yolov5.utils.torch_utils import select_device
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from pymongo import MongoClient

#All IMPORT
import torch
import pymongo
import base64
import gridfs
import json
import gridfs

from pymongo import MongoClient
from django.conf import settings
import gridfs
from django.shortcuts import render

def index(request):
    return render(request,'index.html')


print(torch.cuda.is_available())


confidence = None
check = True
end=True
det=0

connect_str = "mongodb+srv://ilay:asis2003@cluster0.2mtny9z.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient("mongodb+srv://ilay:asis2003@cluster0.2mtny9z.mongodb.net/?retryWrites=true&w=majority")
connect = MongoClient(connect_str) 


def mongo_connection():
    connect_str = "mongodb+srv://ilay:asis2003@cluster0.2mtny9z.mongodb.net/?retryWrites=true&w=majority"
    try:
        connect = MongoClient(connect_str)
        print("Connect Succeed !",connect)
        return connect.Rocket
    except Exception as err:
        print("Error connecting" + Exception)


def update_metadata(file_id, metadata):
    # Connect to the MongoDB database
    # connect_str = "mongodb+srv://ilay:asis2003@cluster0.2mtny9z.mongodb.net/?retryWrites=true&w=majority"
    # client = pymongo.MongoClient(connect_str)
    # db = client["Rocket"]
    db = client[settings.DATABASES['default']['NAME']]
    fs = gridfs.GridFS(db, collection="VideosDetection")

    # Update the metadata for the file with the given ID
    try:
        result = fs.VideosDetection.files.update_one(
            {"_id": file_id},
            {"$set": {"metadata": metadata}}
        )
        print("Metadata updated successfully")
    except Exception as e:
        print("Error updating metadata: ", e)

def get_files(request):
    # connect_str = settings.DATABASES['default']['CLIENT']['host']
    print("connect_str",connect_str)
    # connect = MongoClient(connect_str)
    print("connect",connect)
    # db = connect.get_database(settings.DATABASES['default']['NAME'])

    db = client[settings.DATABASES['default']['NAME']]
    print("db",db)
    fs = gridfs.GridFS(db, collection="VideosDetection")
    # Find all the files in the database
    files = fs.find()

    data = []
    # Iterate through the files and extract the metadata and filename
    for file in files:
        metadata = file.metadata
        filename = file.filename
    
        # Convert the binary data in the metadata to a base64-encoded string
        if 'Image' in metadata:
            image_data = metadata['Image']
            metadata['Image'] = base64.b64encode(image_data).decode('utf-8')

        data.append({'filename': filename, 'metadata': metadata})

    # Return the data as a JSON response
    return HttpResponse(json.dumps(data), content_type='application/json')


@csrf_exempt
def load_video(request):
    if request.method == 'GET':
        
        #get the fileName
        fileName = request.GET.get('filename','FailedGetFileName')
        #connect to db
        # connect_str = settings.DATABASES['default']['CLIENT']['host']
        print("connect_str",connect_str)
        # connect = MongoClient(connect_str)
        print("connect",connect)
        # db = connect.get_database(settings.DATABASES['default']['NAME'])
        db = client[settings.DATABASES['default']['NAME']]
        print("db",db)
        fs = gridfs.GridFS(db, collection="VideosDetection")
        #fine the spesific file
        file = fs.find_one({"filename": fileName})
        if file is None:
            return HttpResponse(status=404)
        print("i make a response with the video file" ,fileName )

        response = HttpResponse()
        response['Content-Type'] = 'application/json'

        # read the file contents into a variable
        file_contents = file.read()
        # encode the binary data as a base64 string
        file_contents_base64 = base64.b64encode(file_contents).decode('utf-8')

        detection_data = fs.find_one({"filename": fileName}).metadata['Data']
       
        # convert the detection data to a JSON-formatted string
        detection_data_json = json.dumps(detection_data)
        print("Data",detection_data_json)

        # create a dictionary with the video and detection data
        response_data = {'video': file_contents_base64, 'Data': detection_data_json}
        print(response_data)

        # return the response as JSON
        return HttpResponse(json.dumps(response_data), content_type='application/json')


# def stream(source,startVideo):
#     end = False
#     detection_data = []
#     if startVideo : 
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
#         fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
#         # imageWidth = int(cap.get(3))
#         # imageHeight = int(cap.get(4))
#         # fps = cap.get(cv2.CAP_PROP_FPS)
#         out = cv2.VideoWriter(laoction_name,fourcc,30,(416, 416))
#         cap = cv2.VideoCapture(url)
#         #cap.set(cv2.CAP_PROP_FPS, 120) 
#         cap.set(cv2.CAP_PROP_CONVERT_RGB, 1)
#         cap.set(cv2.CAP_PROP_FPS, 90) 
#         print("Source",source)
#         print("video_name",video_name)
#         print("laoction_name",laoction_name)
#         print("url",url)
#         path_uplode_video_withDetrction = (path_to_save_video) + (saveName)
#         model.conf=0.355
#         flagTime = True
#         while (cap.isOpened()):
#             if(flagTime):
#                 startS = time.time()
#                 flagTime = False
#             check = True
#             ret, frame = cap.read()
#             start_time = time.perf_counter()
#             if not ret:
#                 print("Error: failed to capture image")
#                 check = False
#                 print(str('Completed video ') + str(saveName))
#                 endE = time.time()
#                 break
#             frame = cv2.resize(frame, (320, 320))
#             frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#             results = model(frame,augment=False,size=320)
#             end_time = time.perf_counter()
#             fps = 1 / np.round(end_time - start_time, 3)
#             print("FPS :" , fps)
#             det = results.pred[0]
#             results.render()
#             #out.write(frame)   
#             for *xyxy, conf, cls in det:
#                 floatNum=torch.IntTensor.item(conf)
#                 num=f"{floatNum:.2f}"
#                 detection_conf = float(num)
#                 confidence = detection_conf
#                 path_to_frame =  "C:/Users/ilaya/LaunchVideos/Frame/BestFrameFor" +  str(saveName) + ".jpg"
#                 # if confidence > 0.6:
#                 #     cv2.imwrite(path_to_frame,frame)
#                 # end = time.time()
#                 time_to_detect = 0
#                 x1 = int(xyxy[0].item())
#                 y1 = int(xyxy[1].item())
#                 x2 = int(xyxy[2].item())
#                 y2 = int(xyxy[3].item())
#                 width = x2 - x1
#                 height = y2 - y1
#                 surface_area = width * height
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
#                         b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n')
#         cap.release()
#         out.release()
#         elapsed_time_ms = ( endE - startS ) 
#         print("time",elapsed_time_ms)
#         # print("frame_counter",frame_counter)
#         cv2.destroyAllWindows()
#         # json_file_name = "detection_data_" + str(saveNameJson)+str(".json")
#         # with open(json_file_name, "w") as f:
#         #     json.dump(detection_data, f)
#         end = True
#         # print("json_file_name",json_file_name)
#         # print("file_loc at end",file_loc,"filename",file_name)
#     if end:
#         print("done")
#         startVideo = False
#         # upload_video_file_toMongo(file_loc=file_loc,file_name=file_name,json_file=json_file_name,path_to_frame=path_to_frame)





# @csrf_exempt
# def video_feed(request):
#     if request.method == 'POST':
#         global startvideo
#         global content
#         global start
#         startvideo=True
#         content = request.GET.get('url','not')
#         print(content)  
#     return StreamingHttpResponse(stream(content,startvideo), content_type='multipart/x-mixed-replace; boundary=frame')  



# def detection():
#     while True:
#         if(not check):
#             data={"isRunning":False,"passtime":time_to_detect}
#             dataJson=json.dumps(data)        
#             return dataJson
#         if(confidence is not None  and len(det) > 0):
#             data={"det":confidence,"isRunning":True,"passtime":time_to_detect}
#             dataJson=json.dumps(data)
#             return dataJson
#         data={"isRunning":True}
#         dataJson=json.dumps(data) 
#         return dataJson




# def upload_video_file_toMongo(file_loc,file_name,json_file,path_to_frame):
#     print("file loc at upload_video_file_toMongo",file_loc)
#     print("path_to_frame",path_to_frame)
#     now = datetime.datetime.now()

#     formatted_date_time = now.strftime("%Y-%m-%d / %H:%M")
#     db = mongo_connection()
#     fs = gridfs.GridFS(db,collection="VideosDetection")

#     with open(file_loc,'rb') as file_data:
#         data = file_data.read()
#     with open(json_file, "r") as f:
#         json_data = json.load(f)    
#     with open(path_to_frame, "rb") as f:
#         image_data = f.read()

#     metadata = {
#         "Data": json_data,
#         "Image": image_data,
#         "Date":formatted_date_time
#     }

#     #Check if a file with the same name already exists in the collection
#     existing_file = fs.find_one({"filename": file_name})

#     # Update the file if it already exists
#     if existing_file is not None:
#         # Delete the existing file
#         fs.delete(existing_file._id)
#         #Re-upload the file with the new data and metadata
#         fs.put(data, filename=file_name, metadata=metadata)
#         print("File updated successfully")
#     else:
#         # Add the new file to the collection
#         fs.put(data, filename=file_name, metadata=metadata)
#         print("File added successfully")



#load model

#model = torch.hub.load('ultralytics/yolov','custom',path='C:/Users/ilaya/trainningModels/TREX2FitWithin/best.pt',device=device)
#model = torch.hub.load('ultralytics/yolov5', 'custom',path='C:/Users/ilaya/trainningModels/TREX2Base/best.pt',device=device)
#model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:/Users/ilaya/trainningModels/Rocket-Detect-32/300epmodel5n/best.pt',device=device)
# model = YOLO(path='C:/Users/ilaya/trainningModels/TREX2Base/best.pt')
#model = torch.hub.load('ultralytics/yolov8', 'custom', path='C:/Users/ilaya/trainningModels/Rocket-Detect-27/best.pt',)
#model = torch.hub.load('ultralytics/yolov5', 'yolov5s','yolov5s.onnx')
#model = torch.hub.load('ultralytics/yolov5', 'custom',path='C:/Users/ilaya/trainningModels/TREX2FitWithin/best.pt',device=device)
# initialize deepsort
# cfg = get_config()
# cfg.merge_from_file("deep_sort/configs/deep_sort.yaml")
# deepsort = DeepSort('osnet_x0_25',
#                     device,
#                     max_dist=cfg.DEEPSORT.MAX_DIST,
#                     max_iou_distance=cfg.DEEPSORT.MAX_IOU_DISTANCE,
#                     max_age=cfg.DEEPSORT.MAX_AGE, n_init=cfg.DEEPSORT.N_INIT, nn_budget=cfg.DEEPSORT.NN_BUDGET,
#                     )
# global num_frames,elapsed_time,start_time
# num_frames = 0
# elapsed_time = 0
# start_time = time.perf_counter()
# Get names and colors




# from asgiref.sync import async_to_sync
# from channels.layers import get_channel_layer
# import time
# from channels.generic.websocket import AsyncWebsocketConsumer
# from multiprocessing import Process
# from bson.objectid import ObjectId
# from deep_sort.deep_sort import DeepSort
# from djongo.storage import GridFSStorage
# from django.views import View
# from gridfs import GridFSBucket
# from threading import Thread
# from PIL import Image as im
# from zipfile import ZipFile
# from yolov5 import detect
# from mydia import Videos
# from io import BytesIO
# from ast import While
# import pickle
# import logging
# import urllib
# import sys
# import os
# import onnx
# import datetime
# import pafy
# import cv2
# import sys
#import cv2, pickle

# from django.views.decorators.http import require_http_methods
# from django.views.decorators.http import require_GET
# from deep_sort.utils.parser import get_config
# from urllib.parse import urlparse,parse_qs
#import asyncio

# model = torch.hub.load('ultralytics/yolov5', 'custom',path='C:/Users/ilaya/trainningModels/pro/best.pt',device=device)
# names = model.module.names if hasattr(model, 'module') else model.names

#import numpy as np
#device = select_device('0') # 0 for gpu, '' for cpu