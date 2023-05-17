# # from django.shortcuts import render
# from ast import arg
# from django.http import HttpResponse


# # import yolov5
# # import torch
# # from PIL import Image as im
# import sched, time
# # from yolov5.utils.general import (LOGGER,check_img_size, non_max_suppression, scale_coords, 
# #                                   check_imshow, xyxy2xywh, increment_path)
# # from yolov5.utils.torch_utils import select_device, time_sync
# # from yolov5.utils.plots import Annotator, colors
# # from deep_sort.utils.parser import get_config
# # from deep_sort.deep_sort import DeepSort
# # from django.http import JsonResponse
# # from django.http import HttpResponse

# # import cv2
# # from twisted.internet import task, reactor
# # def index(request):
# #     return render(request,'index.html')
# # # def indexconf(request):
# # #     return render(request,'index.html')

# # #load model
# # #model = yolov5.load('yolov5s.pt')
# # model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:/Users/ilaya/trainningModels/TREX2Base/best.pt')

# # device = select_device('') 

# # cfg = get_config()

# # cfg.merge_from_file("deep_sort/configs/deep_sort.yaml")
# # deepsort = DeepSort('osnet_x0_25',
# #                     device,
# #                     max_dist=cfg.DEEPSORT.MAX_DIST,
# #                     max_iou_distance=cfg.DEEPSORT.MAX_IOU_DISTANCE,
# #                     max_age=cfg.DEEPSORT.MAX_AGE, n_init=cfg.DEEPSORT.N_INIT, nn_budget=cfg.DEEPSORT.NN_BUDGET,
# #                     )

# # names = model.module.names if hasattr(model, 'module') else model.names


# # source = cv2.VideoCapture("LaunchC2.mp4")

        
# # # def details():
# # #      ret,frame = source.read()
# # #      results=model(frame,augment=True)
# # #      labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1].numpy()
# # #      print(results,cord)
     
# # #      det = results.pred[0]
# # #      for *xyxy, conf, cls in det:
# # #            #print(conf.item())
# # #            num=torch.IntTensor.item(conf)
# # #            if(type(num)==float):

# # #                 floatNum=torch.IntTensor.item(conf)
# # #                 num=f"{floatNum:.2f}"
# # #                 yield num
# # #                 if(num is not None):
# # #                     yield num
# # #                 else:
# # #                     yield None
                      
    
# # def details():
    
# #      ret,frame = source.read()
# #      results=model(frame,augment=True)
# #      labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1].numpy()
# #      det = results.pred[0]
# #      for *xyxy, conf, cls in det:
# #            num=torch.IntTensor.item(conf)
# #            floatNum=torch.IntTensor.item(conf)
# #            num=f"{floatNum:.2f}"
# #            numFloaf = float(num)
           
# #            return 0 if num is None else numFloaf    

# # def stream():
# #     while (source.isOpened()):
# #         ret,frame = source.read()
# #         # test_image = source.open(ret).convert('RGB')
# #         # print(test_image)
# #         if not ret:
# #             print("Erorr:faild to capture image")
# #             break
        
# #         results=model(frame,augment=True)

# #         #proccess
# #         #annotator=Annotator(frame,line_width=2,pil=not ascii)
# #         for i in results.render():
           
# #             data=im.fromarray(i)
# #             data.save('demo.jpg')
       
    
# #         #cv2.imshow('demo.jpg',frame)

# #         #image_bytes=cv2.imencode('.jpg',frame)[1].tobytes()
# #         yield (b'--frame\r\n'
# #                b'Content-Type: image/jpeg\r\n\r\n' + open('demo.jpg','rb').read() + b'\r\n')     

# # # def conf():
# # #     while(True):
# # #         if(details() is not None):
# # #             yield details()
# # #             yield ("\n")
# # #         else:
# # #             yield 0

# # # def conf():
# # #     while(True):
# # #       yield ("\n")
# # #       yield details().to_json

        
         
# # def detection_percentage(request):
# #     return StreamingHttpResponse(conf())
    
# # def video_feed(request):
# #     return StreamingHttpResponse(stream(),content_type='multipart/x-mixed-replace; boundary=frame')
# # def conf():
# #     while(True):
# #          yield details()

# ###hehre

# # s = sched.scheduler(time.time, time.sleep)
# # def conf(sc): 
# #     yield details()
# #     # do your stuff
# #     sc.enter(60, 1, conf, (sc,))

# # s.enter(1, 1, conf, (s,))
# # s.run()
         



# # timeout = 1.0 # Sixty seconds

# # # def doWork():
# # #     while True:
# # #       yield(details())
# # #       time.sleep(0.001)  
      
  


# # def detection_percentage(request):
# #     return StreamingHttpResponse(conf(),content_type='text-plain')

# # def details_a(request):
# #     return StreamingHttpResponse(details(),content_type='text-plain')
# # def details_a(request):
# #     return HttpResponse(details(),content_type='multipart/x-mixed-replace')

# # def detaction():
# #     ret,frame = source.read()
# #     results=model(frame,augment=True)
# #     labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]
# #     n = len(labels)
# #     for i in range(n):
# #         row = cord[i]
        
# #         conf=row.detach().numpy()[4]
# #         floatNum = "{:.2f}".format(conf)
# #         confItem= str(floatNum)
# #         print(confItem)

# # from django.shortcuts import render
# # from django.http import StreamingHttpResponse
# # import yolov5,torch
# # from yolov5.utils.general import (check_img_size, non_max_suppression, scale_coords, 
# #                                   check_imshow, xyxy2xywh, increment_path)
# # from yolov5.utils.torch_utils import select_device, time_sync
# # from yolov5.utils.plots import Annotator, colors
# # from deep_sort.utils.parser import get_config
# # from deep_sort.deep_sort import DeepSort
# # import cv2
# # from PIL import Image as im
# # # Create your views here.
# # def index(request):
# #     return render(request,'index.html')
# # print(torch.cuda.is_available())
# # #load model
# # #model = yolov5.load('yolov5s.pt')
# # model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:/Users/ilaya/trainningModels/TREX2Base/best.pt')
# # #model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
# # device = select_device('') # 0 for gpu, '' for cpu
# # # initialize deepsort
# # cfg = get_config()
# # cfg.merge_from_file("deep_sort/configs/deep_sort.yaml")
# # deepsort = DeepSort('osnet_x0_25',
# #                     device,
# #                     max_dist=cfg.DEEPSORT.MAX_DIST,
# #                     max_iou_distance=cfg.DEEPSORT.MAX_IOU_DISTANCE,
# #                     max_age=cfg.DEEPSORT.MAX_AGE, n_init=cfg.DEEPSORT.N_INIT, nn_budget=cfg.DEEPSORT.NN_BUDGET,
# #                     )
# # # Get names and colors
# # names = model.module.names if hasattr(model, 'module') else model.names

# # source = cv2.VideoCapture("LaunchC2.mp4") 

# # def details(): 
# #      ret,frame = source.read()
# #      results=model(frame,augment=True)
# #      labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1].numpy()
# #      det = results.pred[0]
# #      for *xyxy, conf, cls in det:
# #            num=torch.IntTensor.item(conf)
# #            floatNum=torch.IntTensor.item(conf)
# #            num=f"{floatNum:.2f}"
# #            numFloaf = float(num)
           
# #            return 0 if num is None else numFloaf    

# # def stream():
# #     while (source.isOpened()):
# #         ret, frame = source.read()
# #         print(ret)
# #         if not ret:
# #             print("Error: failed to capture image")
# #             break

# #         results = model(frame, augment=True)
# #         print(results)
# #         print(type(results))
# #         # proccess
# #         annotator = Annotator(frame, line_width=2, pil=not ascii) 
# #         print(annotator)
# #         det = results.pred[0]
# #         if det is not None and len(det):   
# #             xywhs = xyxy2xywh(det[:, 0:4])
# #             confs = det[:, 4]
# #             clss = det[:, 5]
# #             outputs = deepsort.update(xywhs.cpu(), confs.cpu(), clss.cpu(), frame)
# #             if len(outputs) > 0:
# #                 for j, (output, conf) in enumerate(zip(outputs, confs)):

# #                     bboxes = output[0:4]
# #                     id = output[4]
# #                     cls = output[5]

# #                     c = int(cls)  # integer class
# #                     label = f'{id} {names[c]} {conf:.2f}'
# #                     annotator.box_label(bboxes, label, color=colors(c, True))

# #         else:
# #             deepsort.increment_ages()

# #         im0 = annotator.result() 
# #         print(type(im0))
# #         image_bytes = cv2.imencode('.jpg', im0)[1].tobytes()
# #         # co=cv2.imdecode('.jpg', confs)[1].tobytes()
        
# #         yield (b'--frame\r\n'
# #                b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n')  


       
# # def detection_percentage(request):
# #     return StreamingHttpResponse(conf())

# # def video_feed(request):
# #     return StreamingHttpResponse(stream(), content_type='multipart/x-mixed-replace; boundary=frame')




# #            return 0 if num is None else numFloaf    


# # #####################
# # from django.shortcuts import render
# # from django.http import StreamingHttpResponse,HttpResponseServerError
# # import yolov5,torch
# # from yolov5.utils.general import (check_img_size, non_max_suppression, scale_coords, 
# #                                   check_imshow, xyxy2xywh, increment_path)
# # from yolov5.utils.torch_utils import select_device, time_sync
# # from yolov5.utils.plots import Annotator, colors
# # from deep_sort.utils.parser import get_config
# # from deep_sort.deep_sort import DeepSort
# # from threading import Thread
# # import cv2, time
# # from PIL import Image as im
# # from django.views.decorators import gzip
# # # Create your views here.
# # def index(request):
# #     return render(request,'index.html')
# # print(torch.cuda.is_available())
# # from django.views.decorators import gzip
# # import numpy as np
# # #load model
# # #model = yolov5.load('yolov5s.pt')
# # model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:/Users/ilaya/trainningModels/TREX2Base/best.pt')
# # #model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
# # device = select_device('') # 0 for gpu, '' for cpu
# # # initialize deepsort
# # cfg = get_config()
# # cfg.merge_from_file("deep_sort/configs/deep_sort.yaml")
# # deepsort = DeepSort('osnet_x0_25',
# #                     device,
# #                     max_dist=cfg.DEEPSORT.MAX_DIST,
# #                     max_iou_distance=cfg.DEEPSORT.MAX_IOU_DISTANCE,
# #                     max_age=cfg.DEEPSORT.MAX_AGE, n_init=cfg.DEEPSORT.N_INIT, nn_budget=cfg.DEEPSORT.NN_BUDGET,
# #                     )
# # # Get names and colors
# # names = model.module.names if hasattr(model, 'module') else model.names

# # source = cv2.VideoCapture("launch5.mp4") 
# # #source.set(cv2.CAP_PROP_BUFFERSIZE, 2)



# # def stream():
# #     while (source.isOpened()):
       
# #         ret, frame = source.read()
       
        
# #         print(ret)
# #         if not ret:
# #             print("Error: failed to capture image")
# #             break

# #         results = model(frame, augment=True)
# #         print(results)
# #         # proccess
# #         annotator = Annotator(frame, line_width=2, pil=not ascii) 
# #         det = results.pred[0]
# #         if det is not None and len(det):   
# #             xywhs = xyxy2xywh(det[:, 0:4])
# #             confs = det[:, 4]
# #             clss = det[:, 5]
# #             outputs = deepsort.update(xywhs.cpu(), confs.cpu(), clss.cpu(), frame)
# #             if len(outputs) > 0:
# #                 for j, (output, conf) in enumerate(zip(outputs, confs)):
                    

# #                     bboxes = output[0:4]
# #                     # id = output[4]
# #                     cls = output[5]

# #                     c = int(cls)  # integer class
# #                     # label = f'{id} {names[c]} {conf:.2f}'
# #                     label = f'{names[c]} {conf:.2f}'
# #                     cons=f'{conf:.2f}'
# #                     print(cons)
# #                     annotator.box_label(bboxes, label, color=colors(c, True))

# #         else:
# #             deepsort.increment_ages()

# #         im0 = annotator.result()    
# #         image_bytes = cv2.imencode('.jpg', im0)[1].tobytes()
# #         yield (b'--frame\r\n'
    
# #            b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n') 

# # def stream():
# #     while (source.isOpened()):
# #         source.set(cv2.CAP_PROP_BUFFERSIZE, 2)
# #         ret,frame = source.read()
# #         if not ret:
# #             print("Erorr:faild to capture image")
# #             break
# #         results=model(frame,size=640)
# #         #proccess
# #         #annotator=Annotator(frame,line_width=2,pil=not ascii)
# #         for i in results.render():
# #             data=im.fromarray(i)
# #             data.save('demo.jpg')
# #         #cv2.imshow('demo.jpg',frame)

# #         print(results)
# #         #image_bytes=cv2.imencode('.jpg',frame)[1].tobytes()
# #         yield (b'--frame\r\n'
# #                b'Content-Type: image/jpeg\r\n\r\n' + open('demo.jpg','rb').read() + b'\r\n')
# # def video_feed(request):
# #     return StreamingHttpResponse(stream(),content_type='multipart/x-mixed-replace; boundary=frame')

# # def stream():
# #     capture=cv2.VideoCapture("LaunchC2.mp4")
# #     capture.set(cv2.CAP_PROP_BUFFERSIZE, 2)
# #     FPS = 1/30
# #     #FPS_MS = int(FPS * 1000)
# #     thread = Thread(target=capture.isOpened(),args=())
# #     thread.daemon = True
# #     thread.start()
# #     while (capture.isOpened()):  
# #         if capture.isOpened():
# #             (status, frame) =capture.read()
# #         time.sleep(FPS)
# #         ret, frame = capture.read()  
# #         print("ret",ret)
# #         if not ret:
# #             print("Error: failed to capture image")
# #             break   
# #         results = model(frame,size=640)
# #         print("results",results)
# #         # proccess
# #         annotator = Annotator(frame, line_width=2, pil=not ascii) 
# #         det = results.pred[0]
# #         if det is not None and len(det):   
# #             xywhs = xyxy2xywh(det[:, 0:4])
# #             confs = det[:, 4]
# #             clss = det[:, 5]
# #             outputs = deepsort.update(xywhs.cpu(), confs.cpu(), clss.cpu(), frame)
# #             if len(outputs) > 0:
# #                 for j, (output, conf) in enumerate(zip(outputs, confs)):
# #                     bboxes = output[0:4]
# #                     # id = output[4]
# #                     cls = output[5]
# #                     c = int(cls)  # integer class
# #                     # label = f'{id} {names[c]} {conf:.2f}'
# #                     label = f'{names[c]} {conf:.2f}'
# #                     cons=f'{conf:.2f}'
# #                     print(cons)
# #                     annotator.box_label(bboxes, label, color=colors(c, True))
# #         else:
# #             deepsort.increment_ages()
# #         im0 = annotator.result()    
# #         image_bytes = cv2.imencode('.jpg', im0)[1].tobytes()
# #         yield (b'--frame\r\n'
# #                b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n') 
# # def conf():
# #     capture=cv2.VideoCapture("LaunchC2.mp4")
# #     capture.set(cv2.CAP_PROP_BUFFERSIZE, 2)
    
# #     FPS = 1/30
# #     FPS_MS = int(FPS * 1000)
# #     thread = Thread(args=())
# #     thread.daemon = True
# #     thread.start()
    
# #     while (capture.isOpened()):
# #         if capture.isOpened():
# #             (ret, frame) =capture.read()
# #         time.sleep(FPS)
# #         if not ret:
# #             print("Error: failed to capture image")
# #             break
# #         results=model(frame,augment=True)
# #         det = results.pred[0]
# #         if det is not None and len(det):   
# #             xywhs = xyxy2xywh(det[:, 0:4])
# #             confs = det[:, 4]
# #             clss = det[:, 5]
# #             outputs = deepsort.update(xywhs.cpu(), confs.cpu(), clss.cpu(), frame)
# #             for j, (output, conf) in enumerate(zip(outputs, confs)):
# #                     bboxes = output[0:4]
# #                     id = output[4]
# #                     cls = output[5]
# #                     c = int(cls)  # integer class
# #                     label = f'{id} {names[c]} {conf:.2f}'
# #                     confObj=f'{conf:.2f}'
# #                     return confObj

# # @gzip.gzip_page
# # def video_feed(request):
# #         return StreamingHttpResponse(stream(), content_type='multipart/x-mixed-replace; boundary=frame')  

           
# # def detection_percentage(request):
# #      return StreamingHttpResponse(conf())   
# # def video_feed(request):
# #     return StreamingHttpResponse(stream(), content_type='multipart/x-mixed-replace; boundary=frame')  





# # from threading import Thread
# # import cv2, time

# # class ThreadedCamera:
# #     def __init__(self, src):
# #       c
# #         # FPS = 1/X
# #         # X = desired FPS
# #         self.FPS = 1/30
# #         self.FPS_MS = int(self.FPS * 1000)
        
# #         # Start frame retrieval thread
# #         self.thread = Thread(target=self.update, args=())
# #         self.thread.daemon = True
# #         self.thread.start()
        
# #     def update(self):
# #         while True:
# #             if self.capture.isOpened():
# #                 (self.status, self.frame) = self.capture.read()
# #             time.sleep(self.FPS)
            
# #     def show_frame(self):
# #         cv2.imshow('frame', self.frame)
# #         cv2.waitKey(self.FPS_MS)

# # if __name__ == '__main__':
# #     src = 'LaunchC2.mp4'
# #     threaded_camera = ThreadedCamera(src)
# #     while True:
# #         try:
# #             threaded_camera.show_frame()
# #         except AttributeError:
# #             pass



# # from django.shortcuts import render
# # from django.http import StreamingHttpResponse,HttpResponseServerError
# # import yolov5,torch
# # from yolov5.utils.general import (check_img_size, non_max_suppression, scale_coords, 
# #                                   check_imshow, xyxy2xywh, increment_path)
# # from yolov5.utils.torch_utils import select_device, time_sync
# # from yolov5.utils.plots import Annotator, colors
# # from deep_sort.utils.parser import get_config
# # from deep_sort.deep_sort import DeepSort
# # import cv2, time
# # from PIL import Image as im
# # from django.views.decorators import gzip
# # # Create your views here.
# # def index(request):
# #     return render(request,'index.html')
# # print(torch.cuda.is_available())
# # from django.views.decorators import gzip
# # import numpy as np
# # #load model
# # #model = yolov5.load('yolov5s.pt')
# # model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:/Users/ilaya/trainningModels/TREX2Base/best.pt')
# # #model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
# # device = select_device('') # 0 for gpu, '' for cpu
# # # initialize deepsort
# # cfg = get_config()
# # cfg.merge_from_file("deep_sort/configs/deep_sort.yaml")
# # deepsort = DeepSort('osnet_x0_25',
# #                     device,
# #                     max_dist=cfg.DEEPSORT.MAX_DIST,
# #                     max_iou_distance=cfg.DEEPSORT.MAX_IOU_DISTANCE,
# #                     max_age=cfg.DEEPSORT.MAX_AGE, n_init=cfg.DEEPSORT.N_INIT, nn_budget=cfg.DEEPSORT.NN_BUDGET,
# #                     )
# # # Get names and colors
# # names = model.module.names if hasattr(model, 'module') else model.names

# # source = cv2.VideoCapture("LaunchC2.mp4") 


      


# # def conf():
# #     while (source.isOpened()):
# #         ret, frame = source.read()
# #         if not ret:
# #             print("Error: failed to capture image")
# #             break
# #         results = model(frame, augment=True)
# #         det = results.pred[0]
# #         if det is not None and len(det):   
# #             xywhs = xyxy2xywh(det[:, 0:4])
# #             confs = det[:, 4]
# #             clss = det[:, 5]
# #             outputs = deepsort.update(xywhs.cpu(), confs.cpu(), clss.cpu(), frame)
# #             if len(outputs) > 0:
# #                 for j, (output, conf) in enumerate(zip(outputs, confs)):
                    

# #                     bboxes = output[0:4]
# #                     id = output[4]
# #                     cls = output[5]

# #                     c = int(cls)  # integer class
# #                     label = f'{id} {names[c]} {conf:.2f}'
# #                     cons=f'{conf:.2f}'
# #                     return cons
           
    
# # def detection_percentage(request):
# #      return StreamingHttpResponse(conf())

# # def video_feed(request):
# #     return StreamingHttpResponse(stream(), content_type='multipart/x-mixed-replace; boundary=frame')  

# # def details():
    
# #      ret,frame = source.read()
# #      results=model(frame,augment=True)
# #      labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1].numpy()
# #      det = results.pred[0]
# #      for *xyxy, conf, cls in det:
# #            num=torch.IntTensor.item(conf)
# #            floatNum=torch.IntTensor.item(conf)
# #            num=f"{floatNum:.2f}"
# #            numFloaf = float(num)
           
# #            return 0 if num is None else numFloaf   
# # 
# # 
# # # def stream():
# #     while (source.isOpened()):
# #         ret, frame = source.read()
# #         print(ret)
# #         if not ret:
# #             print("Error: failed to capture image")
# #             break

# #         results = model(frame, augment=True)
# #         print(results)
# #         # proccess
# #         annotator = Annotator(frame, line_width=2, pil=not ascii) 
# #         det = results.pred[0]
# #         if det is not None and len(det):   
# #             xywhs = xyxy2xywh(det[:, 0:4])
# #             confs = det[:, 4]
# #             clss = det[:, 5]
# #             outputs = deepsort.update(xywhs.cpu(), confs.cpu(), clss.cpu(), frame)
# #             if len(outputs) > 0:
# #                 for j, (output, conf) in enumerate(zip(outputs, confs)):
                    

# #                     bboxes = output[0:4]
# #                     id = output[4]
# #                     cls = output[5]

# #                     c = int(cls)  # integer class
# #                     label = f'{id} {names[c]} {conf:.2f}'
# #                     cons=f'{conf:.2f}'
# #                     print(cons)
# #                     annotator.box_label(bboxes, label, color=colors(c, True))

# #         else:
# #             deepsort.increment_ages()

# #         im0 = annotator.result()    
# #         image_bytes = cv2.imencode('.jpg', im0)[1].tobytes()
# #         yield (b'--frame\r\n'
# #                b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n') 

# # def stream():
# #     cap=cv2.VideoCapture("RocketLunch2.mp4")
# #     #model.conf=0.1
# #     #model.iou=0.5
# #     while (True):
# #         ret, frame = cap.read()
# #         if not ret:
# #             print("Error: failed to capture image")
# #             break
# #         results = model(frame,augment=True)
# #         print(results)
# #         # proccess
# #         annotator = Annotator(frame, line_width=2, pil=not ascii) 
# #         det = results.pred[0]
# #         #cos = det[:, 4]
# #         #xywhs = xyxy2xywh(det[:, 0:4])
        
# #         if det is not None and len(det):   
# #             xywhs = xyxy2xywh(det[:, 0:4])
# #             confs = det[:, 4]
# #             clss = det[:, 5]
# #             outputs = deepsort.update(xywhs.cpu(), confs.cpu(), clss.cpu(), frame)
# #             #outputs = deepsort.update(xywhs, confs, clss, frame)
# #             for j, (output, conf) in enumerate(zip(outputs, confs)):
                    
# #                     bboxes = output[0:4]
# #                     #id = output[4]
# #                     cls = output[5]
# #                     print(cls,"cls")

# #                     c = int(cls)  # integer class
# #                     label = f'{names[c]} {conf:.2f}'
# #                     cons=f'{conf:.2f}'
# #                     print(cons)
# #                     annotator.box_label(bboxes, label, color=colors(c, True))


#         # im0 = annotator.result()
#         # image_bytes = cv2.imencode('.jpg', im0)[1].tobytes()
#         # yield (b'--frame\r\n'
#         #        b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n')
        
  

# # def conf():
# #     while (source.isOpened()):
# #         ret, frame = source.read()
# #         if not ret:
# #             print("Error: failed to capture image")
# #             break
# #         results = model(frame, augment=True)
# #         det = results.pred[0]
# #         if det is not None and len(det):   
# #             xywhs = xyxy2xywh(det[:, 0:4])
# #             confs = det[:, 4]
# #             clss = det[:, 5]
# #             outputs = deepsort.update(xywhs.cpu(), confs.cpu(), clss.cpu(), frame)
# #             if len(outputs) > 0:
# #                 for j, (output, conf) in enumerate(zip(outputs, confs)):
# #                     bboxes = output[0:4]
# #                     #id = output[4]
# #                     cls = output[5]

# #                     c = int(cls)  # integer class
# #                     label = f'{names[c]} {conf:.2f}'
# #                     cons=f'{conf:.2f}'
# #                     return cons
# # def conf():
# #     while (source.isOpened()):
# #         ret, frame = source.read()
# #         if not ret:
# #             print("Error: failed to capture image")
# #             break
# #         results = model(frame, augment=True)
# #         det = results.pred[0]
# #         if det is not None and len(det):   
# #             xywhs = xyxy2xywh(det[:, 0:4])
# #             confs = det[:, 4]
# #             clss = det[:, 5]
# #             outputs = deepsort.update(xywhs.cpu(), confs.cpu(), clss.cpu(), frame)
# #             if len(outputs) > 0:
# #                 for j, (output, conf) in enumerate(zip(outputs, confs)):
                    

# #                     bboxes = output[0:4]
# #                     id = output[4]
# #                     cls = output[5]

# #                     c = int(cls)  # integer class
# #                     label = f'{id} {names[c]} {conf:.2f}'
# #                     cons=f'{conf:.2f}'
# #                     print(cons)
# #                     return cons


# def stream2():
#     cap=cv2.VideoCapture("RocketLunch1.mp4")
#     #model.conf=0.1
#     #model.iou=0.5
#     while (True):
#         ret, frame = cap.read()
#         if not ret:
#             print("Error: failed to capture image")
#             break
#         results = model(frame,augment=False,size=640)
#         print(results)
#         # proccess
#         annotator = Annotator(frame, line_width=2, pil=not ascii) 
#         det = results.pred[0]
#         #cos = det[:, 4]
#         #xywhs = xyxy2xywh(det[:, 0:4])
        
#         if det is not None and len(det):   
#             xywhs = xyxy2xywh(det[:, 0:4])
#             confs = det[:, 4]
#             clss = det[:, 5]
#             outputs = deepsort.update(xywhs.cpu(), confs.cpu(), clss.cpu(), frame)
#             #outputs = deepsort.update(xywhs, confs, clss, frame)
#             for j, (output, conf) in enumerate(zip(outputs, confs)):
                    
#                     bboxes = output[0:4]
#                     #id = output[4]
#                     cls = output[5]
#                     print(cls,"cls")

#                     c = int(cls)  # integer class
#                     label = f'{names[c]} {conf:.2f}'
#                     cons=f'{conf:.2f}'
#                     print(cons)
#                     annotator.box_label(bboxes, label, color=colors(c, True))


#         im0 = annotator.result()
#         image_bytes = cv2.imencode('.jpg', im0)[1].tobytes()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n')
        

#   # def stream():
# #     while (source.isOpened()):
# #         ret,frame = source.read()
# #         test_image = source.open(ret).convert('RGB')
# #         # print(test_image)
# #         if not ret:
# #             print("Erorr:faild to capture image")
# #             break
        
# #         results=model(frame)

# #         #proccess
# #         #annotator=Annotator(frame,line_width=2,pil=not ascii)
# #         for i in results.render():
# #             data=im.fromarray(i)
# #             data.save('demo.jpg')
       
    
# #         #cv2.imshow('demo.jpg',frame)

# #         #image_bytes=cv2.imencode('.jpg',frame)[1].tobytes()
# #         yield (b'--frame\r\n'
# #                b'Content-Type: image/jpeg\r\n\r\n' + open('demo.jpg').read() + b'\r\n')     
          

# from django.shortcuts import render
# from django.http import StreamingHttpResponse,HttpResponse
# from numpy import size
# import yolov5,torch
# from yolov5.utils.general import (check_img_size, non_max_suppression, scale_coords, 
#                                   check_imshow, xyxy2xywh, increment_path)
# from yolov5.utils.torch_utils import select_device, time_sync
# from yolov5.utils.plots import Annotator, colors
# from deep_sort.utils.parser import get_config
# from deep_sort.deep_sort import DeepSort
# import cv2
# from PIL import Image as im

# # Create your views here.
# def index(request):
#     return render(request,'index.html')
# print(torch.cuda.is_available())
# #load model
# model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:/Users/ilaya/trainningModels/TREX2Base/best.pt')
# #model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
# device = select_device('0') # 0 for gpu, '' for cpu
# # initialize deepsort
# print(torch.version.cuda)
# cfg = get_config()

# cfg.merge_from_file("deep_sort/configs/deep_sort.yaml")
# deepsort = DeepSort('osnet_x0_25',
#                     device,
#                     max_dist=cfg.DEEPSORT.MAX_DIST,
#                     max_iou_distance=cfg.DEEPSORT.MAX_IOU_DISTANCE,
#                     max_age=cfg.DEEPSORT.MAX_AGE, n_init=cfg.DEEPSORT.N_INIT, nn_budget=cfg.DEEPSORT.NN_BUDGET,
#                     )

# # Get names and colors
# names = model.module.names if hasattr(model, 'module') else model.names


# source = cv2.VideoCapture("RocketLunch1.mp4") 

# def stream():
#     model.iou=0.5
#     model.conf=0.15
#     while (source.isOpened()):
#         ret, frame = source.read()
#         print(ret)
#         if not ret:
#             print("Error: failed to capture image")
#             break

#         results = model(frame,augment=True,size=640)
#         print(results)
#         for i in results.render():
#             data=im.fromarray(i)
#             data.save('demo.jpg')
       
#         det = results.pred[0]
     
#         annotator = Annotator(frame, line_width=2, pil=not ascii) 
           
#         im0 = annotator.result()    
#         image_bytes = cv2.imencode('.jpg', im0)[1].tobytes()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n') 


# # def details():
# #      ret,frame = source.read()
# #      results=model(frame,augment=True)
# #      labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1].numpy()
# #      det = results.pred[0]
# #      for *xyxy, conf, cls in det:
# #         if det is not None: 
# #            num=torch.IntTensor.item(conf)
# #            floatNum=torch.IntTensor.item(conf)
# #            num=f"{floatNum:.2f}"
# #            numFloaf = float(num)
# #            print(numFloaf)
# #            return numFloaf  
# # def stream():
# #     model.iou=0.5
# #     model.conf=0.15
# #     FPS=1/30

# #     while (source.isOpened()):
        
        
# #         print(torch.cuda.is_available())
# #         ret, frame = source.read()
# #         scale_percent = 60 # percent of original size
# #         width = int(frame.shape[1] * scale_percent / 100)
# #         height = int(frame.shape[0] * scale_percent / 100)
# #         dim = (width, height)
 
# # resize image

#         # resized=cv2.resize(frame,dim,interpolation=cv2.INTER_AREA)
#         # time.sleep(FPS)
#         # if not ret:
#         #     print("Error: failed to capture image")
#         #     break

#         # results = model(resized,augment=False)
#         # results.render()
#         # # for i in results.render():
#         # #     data=im.fromarray(i)
#         # #     data.save('demo.jpg')
       
#         # # det = results.pred[0]
     
#         # annotator = Annotator(resized, line_width=2, pil=not ascii) 
           
#         # im0 = annotator.result()    
#         # image_bytes = cv2.imencode('.jpg', im0)[1].tobytes()
#         # yield (b'--frame\r\n'
#         #        b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n')
# def detect():
#     while (source.isOpened()):
#         ret, frame = source.read()
#         if not ret:
#             print("Error: failed to capture image")
#             break
#         results = model(frame, augment=True,size=640)
#         det = results.pred[0]
#         if det is not None and len(det):   
#             xywhs = xyxy2xywh(det[:, 0:4])
#             confs = det[:, 4]
#             clss = det[:, 5]
#             outputs = deepsort.update(xywhs, confs, clss, frame)
#             if len(outputs) > 0:
#                 for j, (output, conf) in enumerate(zip(outputs, confs)):
#                     bboxes = output[0:4]
#                     id = output[4]
#                     cls = output[5]

#                     c = int(cls)  # integer class
#                     label = f'{id} {names[c]} {conf:.2f}'
#                     cons=f'{conf:.2f}'
#                     print(cons)
#                     return cons
        
       
# # def streamm():
# #     capture=cv2.VideoCapture("RocketLunch3.mp4")
# #     capture.set(cv2.CAP_PROP_BUFFERSIZE, 2)
# #     FPS = 1/30
# #     #FPS_MS = int(FPS * 1000)
# #     thread = Thread(args=())
# #     thread.daemon = True
# #     thread.start()

# #     while (capture.isOpened()): 
# #         if capture.isOpened():
# #             (ret, frame) =capture.read()
# #         time.sleep(FPS)

# #         ret, frame = capture.read()
# #         if not ret:
# #             print("Error: failed to capture image")
# #             break

# #         results = model(frame, augment=True,size=640)
# #         print(results)
# #         # proccess
# #         annotator = Annotator(frame, line_width=2, pil=not ascii) 
# #         det = results.pred[0]
# #         if det is not None and len(det):   
# #             xywhs = xyxy2xywh(det[:, 0:4])
# #             confs = det[:, 4]
# #             clss = det[:, 5]
# #             outputs = deepsort.update(xywhs.cpu(), confs.cpu(), clss.cpu(), frame)
# #             if len(outputs) > 0:
# #                 for j, (output, conf) in enumerate(zip(outputs, confs)):
                    

# #                     bboxes = output[0:4]
# #                     # id = output[4]
# #                     cls = output[5]

# #                     c = int(cls)  # integer class
# #                     # label = f'{id} {names[c]} {conf:.2f}'
# #                     label = f'{names[c]} {conf:.2f}'
# #                     cons=f'{conf:.2f}'
# #                     print(cons)
# #                     annotator.box_label(bboxes, label, color=colors(c, True))

# #         else:
# #             deepsort.increment_ages()

# #         im0 = annotator.result()    
# #         image_bytes = cv2.imencode('.jpg', im0)[1].tobytes()
# #         yield (b'--frame\r\n'
# #                b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n') 
      
     
# # def conf():
# #     model.iou=0.5
# #     model.conf=0.15
# #     while (source.isOpened()):
# #         ret, frame = source.read()
# #         print(ret)
# #         if not ret:
# #             print("Error: failed to capture image")
# #             break

# #         results = model(frame,augment=True,size=640)
# #         print(results)
# #         for i in results.render():
# #             data=im.fromarray(i)
# #             data.save('demo.jpg')
       
# #         det = results.pred[0]
     
# #         if det is not None and len(det):   
# #             xywhs = xyxy2xywh(det[:, 0:4])
# #             confs = det[:, 4]
# #             clss = det[:, 5]
# #             outputs = deepsort.update(xywhs.cpu(), confs.cpu(), frame)
# #             if len(outputs) > 0:
# #                 for j, (output, conf) in enumerate(zip(outputs, confs)):
                    

# #                     bboxes = output[0:4]
# #                     # id = output[4]
# #                     cls = output[5]

# #                     c = int(cls)  # integer class
# #                     # label = f'{id} {names[c]} {conf:.2f}'
# #                     label = f'{names[c]} {conf:.2f}'
# #                     cons=f'{conf:.2f}'
# #                     print(cons)
# #                     return cons

# def conf():
#     while (source.isOpened()):
#         amount=0   
#         ret, frame = source.read()
#         if not ret:
#             print("am",amount)
#             print("Error: failed to capture image")
#             break

#         results = model(frame,augment=False,size=640)
#         #print(results)
#         # proccess
#         det = results.pred[0]
#         print("before",det)
#         if det is not None and len(det):  
#             xywhs = xyxy2xywh(det[:, 0:4])
#             confs = det[:, 4]
#             clss = det[:, 5]
#             outputs = deepsort.update(xywhs, confs, clss, frame)
#             print("after",enumerate(zip(outputs, confs)))
#             for j, (output, conf) in enumerate(zip(outputs, confs)):

#                     detaction= f'{conf:.2f}'
#                     print(detaction)
#                     return detaction 
        
       
            
      
# def video_feed(request):
#     return StreamingHttpResponse(stream(), content_type='multipart/x-mixed-replace; boundary=frame')           


# def detection_percentage(request):
#     return HttpResponse(conf())
     

# def det():
#     model.iou=0.5
#     model.conf=0.15
#     while (source.isOpened()):
#         ret, frame = source.read()
#         if not ret:
#             print("Error: failed to capture image")
#             break
#         results = model(frame, augment=True,size=640)

#         det = results.pred[0]
#         for *xyxy, conf, cls in det:
#            num=torch.IntTensor.item(conf)
#            floatNum=torch.IntTensor.item(conf)
#            if floatNum is not None and len(det):  
#                  num=f"{floatNum:.2f}"
#                  numFloaf = float(num)
       
#                  print(numFloaf)




#30.10


# def stream2(video):
#     cap = cv2.VideoCapture(video)
#     model.conf = 0.1
#     model.iou = 0.5
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             print("Error: failed to capture image")
#             break

#         results = model(frame, augment=True,size=640)
#         # proccess
#         annotator = Annotator(frame, line_width=2, pil=not ascii) 
#         det = results.pred[0]
#         if det is not None and len(det):   
#             xywhs = xyxy2xywh(det[:, 0:4])
#             confs = det[:, 4]
#             clss = det[:, 5]
#             outputs = deepsort.update(xywhs.cpu(), confs.cpu(), clss.cpu(), frame)

#             for j, (output, conf) in enumerate(zip(outputs, confs)):

#                     bboxes = output[0:4]
#                     id = output[4]
#                     cls = output[5]

#                     c = int(cls)  # integer class
#                     label = f'{id} {names[c]} {conf:.2f}'
#                     annotator.box_label(bboxes, label, color=colors(c, True))
#         else:
#             logging.info('No detections')


#         im0 = annotator.result()    
#         image_bytes = cv2.imencode('.jpg', im0)[1].tobytes()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n')  








# # from django.shortcuts import render
# # from ast import arg
# # from django.http import HttpResponse

# # from django.shortcuts import render
# # from django.http import StreamingHttpResponse,HttpResponse
# # from numpy import size
# # import yolov5,torch
# # from yolov5.utils.general import (check_img_size, non_max_suppression, scale_coords, 
# #                                   check_imshow, xyxy2xywh, increment_path)
# # from yolov5.utils.torch_utils import select_device, time_sync
# # from yolov5.utils.plots import Annotator, colors
# # from deep_sort.utils.parser import get_config
# # from deep_sort.deep_sort import DeepSort
# # import cv2
# # from PIL import Image as im
# # from threading import Thread
# # from multiprocessing import Process
# # # Create your views here.
# # def index(request):
# #     return render(request,'index.html')
# # print(torch.cuda.is_available())
# # #load model
# # model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:/Users/ilaya/trainningModels/TREX2Base/best.pt')
# # device = select_device('0') # 0 for gpu, '' for cpu
# # # initialize deepsort
# # cfg = get_config()

# # cfg.merge_from_file("deep_sort/configs/deep_sort.yaml")
# # deepsort = DeepSort('osnet_x0_25',
# #                     device,
# #                     max_dist=cfg.DEEPSORT.MAX_DIST,
# #                     max_iou_distance=cfg.DEEPSORT.MAX_IOU_DISTANCE,
# #                     max_age=cfg.DEEPSORT.MAX_AGE, n_init=cfg.DEEPSORT.N_INIT, nn_budget=cfg.DEEPSORT.NN_BUDGET,
# #                     )

# # # Get names and colors
# # names = model.module.names if hasattr(model, 'module') else model.names


# # source = ("RocketLunch1.mp4") 

# # # def stream():
# # #     cap = cv2.VideoCapture(source)
# # #     model.iou=0.5
# # #     model.conf=0.15
# # #     while (cap.isOpened()):
# # #         ret, frame = source.read()
# # #         if not ret:
# # #             print("Error: failed to capture image")
# # #             break
# # #         results = model(frame,augment=True,size=640)
# # #         for i in results.render():
# # #             data=im.fromarray(i)
# # #             data.save('demo.jpg')
       
# # #         det = results.pred[0]
     
# # #         annotator = Annotator(frame, line_width=2, pil=not ascii) 
           
# # #         im0 = annotator.result()    
# # #         image_bytes = cv2.imencode('.jpg', im0)[1].tobytes()
# # #         yield (b'--frame\r\n'
# # #                b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n') 
# # # def det():
# # #     model.iou=0.5
# # #     model.conf=0.15
# # #     cap = cv2.VideoCapture(source)
# # #     while (cap.isOpened()):
# # #         ret, frame = source.read()
# # #         if not ret:
# # #             print("Error: failed to capture image")
# # #             break
# # #         results = model(frame, augment=True,size=640)

# # #         det = results.pred[0]
# # #         if det is not None and len(det):   
# # #             xywhs = xyxy2xywh(det[:, 0:4])
# # #             confs = det[:, 4]
# # #             clss = det[:, 5]
# # #             outputs = deepsort.update(xywhs.cpu(), confs.cpu(), clss.cpu(), frame)
# # #             if len(outputs) > 0:
# # #                 for j, (output, conf) in enumerate(zip(outputs, confs)):
# # #                     label = f'{conf:.2f}'
# # #                     print(label)
# # #                     return label  
# # def stream():
# #     cap = cv2.VideoCapture(source)
# #     model.iou=0.5
# #     model.conf=0.15
# #     while (True):
# #         ret, frame = cap.read()
# #         if not ret:
# #             print("Error: failed to capture image")
# #             break
# #         results = model(frame,augment=False,size=640)
        
# #         for i in results.render():
# #             data=im.fromarray(i)
# #             data.save('demo.jpg')

# #         annotator = Annotator(frame, line_width=2, pil=not ascii) 
         
# #         im0 = annotator.result()    
# #         image_bytes = cv2.imencode('.jpg', im0)[1].tobytes()
# #         yield (b'--frame\r\n'
# #                b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n') 
# #     cap.release()
# #     cv2.destroyAllWindows()


# # def det():
# #     cap = cv2.VideoCapture(source)
# #     while (True):
# #         ret, frame = cap.read()
# #         if not ret:
# #             print("Error: failed to capture image")
# #             break
# #         results = model(frame, augment=False,size=640)
                    
# #         det = results.pred[0]
# #         if det is not None and len(det):   
# #             xywhs = xyxy2xywh(det[:, 0:4])
# #             confs = det[:, 4]
# #             clss = det[:, 5]
# #             outputs = deepsort.update(xywhs.cpu(), confs.cpu(), clss.cpu(), frame)

# #             for j, (output, conf) in enumerate(zip(outputs, confs)):
# #                     label = f'{conf:.2f}'
# #                     print(label)
# #                     return label
# #     cap.release()
# #     cv2.destroyAllWindows() 

   


# # if __name__ == '__main__':
# #     p1 = Process(target = stream)
# #     p2 = Process(target = det)

# #     p1.start() 
# #     p2.start()


# #     p1.join()
# #     p2.join()



# # def video_feed(request):
# #     return StreamingHttpResponse(stream(), content_type='multipart/x-mixed-replace; boundary=frame')           


# # def detection_percentage(request):
# #     return HttpResponse(det())
      
# # # def DetectionRocket():
# # #     while (source.isOpened()):
# # #         ret, frame = source.read()
# # #         if not ret:
# # #             print("Error: failed to capture image")
# # #             break

# # #         results = model(frame,augment=False,size=640)
# # #         #print(results)
# # #         # proccess
# # #         det = results.pred[0]
# # #         if det is not None and len(det):  
# # #             xywhs = xyxy2xywh(det[:, 0:4])
# # #             confs = det[:, 4]
# # #             clss = det[:, 5]
            
# # #             for j, (conf) in enumerate(zip(confs)):
# # #                 print(conf)
# # #                 yield conf  
      

     

# # # from django.shortcuts import render
# # # from django.http import StreamingHttpResponse
# # # import yolov5,torch
# # # from yolov5.utils.general import (check_img_size, non_max_suppression, scale_coords, 
# # #                                   check_imshow, xyxy2xywh, increment_path)
# # # from yolov5.utils.torch_utils import select_device, time_sync
# # # from yolov5.utils.plots import Annotator, colors
# # # from deep_sort.utils.parser import get_config
# # # from deep_sort.deep_sort import DeepSort
# # # import cv2
# # # from PIL import Image as im
# # # # Create your views here.
# # # def index(request):
# # #     return render(request,'index.html')
# # # print(torch.cuda.is_available())
# # # #load model
# # # model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:/Users/ilaya/trainningModels/TREX2Base/best.pt')
# # # # model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
# # # device = select_device('0') # 0 for gpu, '' for cpu
# # # # initialize deepsort
# # # cfg = get_config()
# # # cfg.merge_from_file("deep_sort/configs/deep_sort.yaml")
# # # deepsort = DeepSort('osnet_x0_25',
# # #                     device,
# # #                     max_dist=cfg.DEEPSORT.MAX_DIST,
# # #                     max_iou_distance=cfg.DEEPSORT.MAX_IOU_DISTANCE,
# # #                     max_age=cfg.DEEPSORT.MAX_AGE, n_init=cfg.DEEPSORT.N_INIT, nn_budget=cfg.DEEPSORT.NN_BUDGET,
# # #                     )
# # # # Get names and colors
# # # names = model.module.names if hasattr(model, 'module') else model.names
# # # source = ("RocketLunch3.mp4") 

# # # def stream():
# # #     cap = cv2.VideoCapture(source)
# # #     # model.conf = 0.15
# # #     # model.iou = 0.5
# # #     while True:
# # #         ret, frame = cap.read()
# # #         if not ret:
# # #             print("Error: failed to capture image")
# # #             break

# # #         results = model(frame, augment=True,size=640)
# # #         print(results.)
# # #         # proccess
# # #         annotator = Annotator(frame, line_width=2, pil=not ascii) 
# # #         det = results.pred[0]
# # #         if det is not None:   
# # #             xywhs = xyxy2xywh(det[:, 0:4])
# # #             confs = det[:, 4]
# # #             clss = det[:, 5]
# # #             outputs = deepsort.update(xywhs.cpu(), confs.cpu(), clss.cpu(), frame)
# # #             for j, (output, conf) in enumerate(zip(outputs, confs)):

# # #                     bboxes = output[0:4]
# # #                     cls = output[5]

# # #                     c = int(cls)  # integer class
# # #                     label = f'{names[c]} {conf:.2f}'
# # #                     annotator.box_label(bboxes, label, color=colors(c, True))

       

# # #         im0 = annotator.result()    
# # #         image_bytes = cv2.imencode('.jpg', im0)[1].tobytes()
# # #         yield (b'--frame\r\n'
# # #                b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n')  

# # # def video_feed(request):
# # #     return StreamingHttpResponse(stream(), content_type='multipart/x-mixed-replace; boundary=frame')    
# # # def detection_percentage(request):
# # #     return StreamingHttpResponse(stream())

# from django.shortcuts import render
# from ast import arg
# from django.http import HttpResponse,HttpResponseBase
# import sched, time

# from django.shortcuts import render
# from django.http import StreamingHttpResponse,HttpResponse
# from numpy import size
# import yolov5,torch
# from yolov5.utils.general import (check_img_size, non_max_suppression, scale_coords,
#                                   check_imshow, xyxy2xywh, increment_path)
# from yolov5.utils.torch_utils import select_device, time_sync
# from yolov5.utils.plots import Annotator, colors
# from deep_sort.utils.parser import get_config
# from deep_sort.deep_sort import DeepSort
# import cv2
# from PIL import Image as im
# from threading import Thread
# from multiprocessing import Process
# # Create your views here.
# def index(request):
#     return render(request,'index.html')
# print(torch.cuda.is_available())
# #load model

# model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:/Users/ilaya/trainningModels/TREX2Base/best.pt')

# device = select_device('0') # 0 for gpu, '' for cpu
# # initialize deepsort
# cfg = get_config()

# cfg.merge_from_file("deep_sort/configs/deep_sort.yaml")
# deepsort = DeepSort('osnet_x0_25',
#                     device,
#                     max_dist=cfg.DEEPSORT.MAX_DIST,
#                     max_iou_distance=cfg.DEEPSORT.MAX_IOU_DISTANCE,
#                     max_age=cfg.DEEPSORT.MAX_AGE, n_init=cfg.DEEPSORT.N_INIT, nn_budget=cfg.DEEPSORT.NN_BUDGET,
#                     )

# # Get names and colors
# names = model.module.names if hasattr(model, 'module') else model.names

# source = ("RocketLunch1.mp4")

#         # if det is not None and len(det):
#         #     results.xyxyn[0][:, :-1]
#         #     print(results.pandas().xyxyn[0].confidence)
        
# def stream():
#     cap = cv2.VideoCapture(source)
#     model.iou=0.5
#     model.conf=0.15
#     while (True):
#         ret, frame = cap.read()
#         if not ret:
#             print("Error: failed to capture image")
#             break
#         results = model(frame,augment=False,size=640)

#         for i in results.render():
#             data=im.fromarray(i)
#             data.save('demo.jpg')

#         det = results.pred[0]
#         for c in det[:, -1].unique():
#                     n = (det[:, -1] == c).sum()  # detections per class
#                     s += f"{n} {names[int(c)]}{'s' * (n > 1)}, "  # add to string
#                     print(c)
       
#         # if det is not None and len(det):
#         #     xywhs = xyxy2xywh(det[:, 0:4])
#         #     confs = det[:, 4]
#         #     clss = det[:, 5]
#         #     outputs = deepsort.update(xywhs.cpu(), confs.cpu(), clss.cpu(), frame)

#         #     for j, (output, conf) in enumerate(zip(outputs, confs)):
#         #             label = f'{conf:.2f}'
#         #             print("s",label)



#         annotator = Annotator(frame, line_width=2, pil=not ascii)

#         im0 = annotator.result()
#         image_bytes = cv2.imencode('.jpg', im0)[1].tobytes()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n')
#     cap.release()
#     cv2.destroyAllWindows()


                      

# def detection():
#     model.iou=0.5
#     model.conf=0.15
#     cap = cv2.VideoCapture(source)
#     while (True):
#         ret, frame = cap.read()
#         if not ret:
#             print("eError: failed to capture image")
#             break
#         results = model(frame, augment=False,size=640)
#         det = results.pred[0]

#         labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]
       
#         det = results.pred[0]
#         if det is not None and len(det):
#             for *xyxy, conf, cls in det:
          
#                 num=torch.IntTensor.item(conf)
#                 if(type(num)==float):

#                   floatNum=torch.IntTensor.item(conf)
#                   num=f"{floatNum:.2f}"
#                   print("n",num)
                 

#         # if det is not None and len(det):
#         #         confidence=results.pandas().xyxyn[0].confidence
#         #         return confidence

#         if det is not None and len(det):
#             xywhs = xyxy2xywh(det[:, 0:4])
#             confs = det[:, 4]
#             clss = det[:, 5]
#             outputs = deepsort.update(xywhs.cpu(), confs.cpu(), clss.cpu(), frame)

#             for j, (output, conf) in enumerate(zip(outputs, confs)):
#                     label = f'{conf:.2f}'
#                     print(label)
#                     return label
                   
                    
          
#     cap.release()   
#     cv2.destroyAllWindows()

# sourcew = cv2.VideoCapture("RocketLunch1.mp4") 

# # def details():
# #      ret,frame = sourcew.read()
# #      results=model(frame,augment=True)
# #      labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]
# #      det = results.pred[0]
# #      if det is not None and len(det):
# #         for *xyxy, conf, cls in det:
# #              #print(conf.item())
# #              num=torch.IntTensor.item(conf)
# #              if(type(num)==float):

# #                 floatNum=torch.IntTensor.item(conf)
# #                 num=f"{floatNum:.2f}"
# #                 print("d",num)
# #                 return num
# #       cap.release()   
# #        cv2.destroyAllWindows()

# # def detection2(): 
# #     ret,frame = source.read()
# #     while (cap.isOpened()):
# #         ret, frame = cap.read()
# #         if not ret:
# #             print("eError: failed to capture image")
# #             break
# #         results = model(frame, augment=False,size=640)
# #         det = results.pred[0]
# #         labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]
       
# #         det = results.pred[0]
    
# #         if det is not None:
# #             for *xyxy, conf in det:
          
# #                 num=torch.IntTensor.item(conf)
# #                 if(type(num)==float):

# #                   floatNum=torch.IntTensor.item(conf)
# #                   num=f"{floatNum:.2f}"
# #                   return num 

    

# if __name__ == '__main__':
#     p1 = Process(target = stream)
#     p2 = Process(target = detection)

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()



# def video_feed(request):
#     return StreamingHttpResponse(stream(), content_type='multipart/x-mixed-replace; boundary=frame')
        
# def detection_percentage(request):
#     return HttpResponse(details())

     

  

  








# from django.shortcuts import render
# from ast import arg
# from django.http import HttpResponse
# import sched, time

# from django.shortcuts import render
# from django.http import StreamingHttpResponse,HttpResponse
# from numpy import size
# import yolov5,torch
# from yolov5.utils.general import (check_img_size, non_max_suppression, scale_coords,
#                                    check_imshow, xyxy2xywh, increment_path)
# from yolov5.utils.torch_utils import select_device, time_sync
# from yolov5.utils.plots import Annotator, colors
# from deep_sort.utils.parser import get_config
# from deep_sort.deep_sort import DeepSort
# import cv2
# from PIL import Image as im
# from threading import Thread
# from multiprocessing import Process
# # Create your views here.
# def index(request):
#      return render(request,'index.html')
# print(torch.cuda.is_available())
#  #load model
# model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:/Users/ilaya/trainningModels/TREX2Base/best.pt') 
# device = select_device('0') # 0 for gpu, '' for cpu
# # initialize deepsort cfg = get_config()

# cfg.merge_from_file("deep_sort/configs/deep_sort.yaml")
# deepsort = DeepSort('osnet_x0_25',
#                      device,
#                      max_dist=cfg.DEEPSORT.MAX_DIST,
#                      max_iou_distance=cfg.DEEPSORT.MAX_IOU_DISTANCE,
#                      max_age=cfg.DEEPSORT.MAX_AGE, n_init=cfg.DEEPSORT.N_INIT, nn_budget=cfg.DEEPSORT.NN_BUDGET,
#                     )

# # Get names and colors
# names = model.module.names if hasattr(model, 'module') else model.names

# source = ("RocketLunch1.mp4")
# def detaction():
#     ret,frame = source.read()
#     results=model(frame,augment=True)
#     labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]
#     n = len(labels)
#     for i in range(n):
#         row = cord[i]
        
#         conf=row.detach().numpy()[4]
#         floatNum = "{:.2f}".format(conf)
#         confItem= str(floatNum)
#         print(confItem)
# def stream():
#     cap = cv2.VideoCapture(source)
#     model.iou=0.5
#     model.conf=0.15
#     while (cap.isOpened()):
#         ret, frame = cap.read()
#         if not ret:
#             print("Error: failed to capture image")
#             break
#         results = model(frame,augment=False,size=640)
#         labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]

#         for i in results.render():
#             data=im.fromarray(i)
#             data.save('demo.jpg')

#         det = results.pred[0]
#         n = len(labels)
#         for i in range(n):
#             row = cord[i]
        
#             conf=row.detach()[4]
#             floatNum = "{:.2f}".format(conf)
#             confItem= str(floatNum)
#             confi(confItem)
#         # if det is not None and len(det): 
#         #     confs = det[:, 4]
#         #     print(confs[0])
            
#         # if det is not None and len(det):   
#         #     confs = det[:, 4]
#         #     outputs = deepsort.update(xywhs.cpu(), confs.cpu(), clss.cpu(), frame)
#         #     if len(outputs) > 0:
#         #         for j, (output, conf) in enumerate(zip(outputs, confs)):

#         #             bboxes = output[0:4]
#         #             id = output[4]
#         #             cls = output[5]

#         #             c = int(cls)  # integer class
#         #             label = f'{id} {names[c]} {conf:.2f}'
#         #             annotator.box_label(bboxes, label, color=colors(c, True))
#         # if det is not None and len(det):
#         #     results.xyxyn[0][:, :-1]
#         #     print(results.pandas().xyxyn[0].confidence)
#         annotator = Annotator(frame, line_width=2, pil=not ascii)

#         im0 = annotator.result()
#         image_bytes = cv2.imencode('.jpg', im0)[1].tobytes()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n')
#     cap.release()
#     cv2.destroyAllWindows()

# def det():
#     model.iou=0.5
#     model.conf=0.15
#     cap = cv2.VideoCapture(source)
#     while (True):
#         ret, frame = cap.read()
#         if not ret:
#             print("Error: failed to capture image")
#             break
#         results = model(frame, augment=False,size=640)
#         det = results.pred[0]

#         # if det is not None and len(det):
#         #         confidence=results.pandas().xyxyn[0].confidence
#         #         return confidence

#         if det is not None and len(det):
#             xywhs = xyxy2xywh(det[:, 0:4])
#             confs = det[:, 4]
#             clss = det[:, 5]
#             outputs = deepsort.update(xywhs.cpu(), confs.cpu(), clss.cpu(), frame)

#             for j, (output, conf) in enumerate(zip(outputs, confs)):
#                     label = f'{conf:.2f}'
#                     print(label)
#                     yield label
#                     yield
#     cap.release()
#     cv2.destroyAllWindows()

# def confi(numbers):
#     yield numbers


         

# if __name__ == '__main__':
#     p1 = Process(target = stream)
#     p2 = Process(target = det)

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

# def video_feed(request):
#     return StreamingHttpResponse(stream(), content_type='multipart/x-mixed-replace; boundary=frame')

# def detection_percentage(request):
#     return HttpResponse(det())
















from django.shortcuts import render
from django.http import StreamingHttpResponse,HttpResponse
import yolov5,torch
from yolov5.utils.general import (check_img_size, non_max_suppression, scale_coords, 
                                  check_imshow, xyxy2xywh, increment_path)
from yolov5.utils.torch_utils import select_device, time_sync
from yolov5.utils.plots import Annotator, colors
from deep_sort.utils.parser import get_config
from deep_sort.deep_sort import DeepSort
import cv2
from PIL import Image as im
# Create your views here
import logging
# .
def index(request):
    return render(request,'index.html',stream())
def index(request):
    return render(request,'detection.html',detection())
print(torch.cuda.is_available())
#load model
#model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:/Users/ilaya/trainningModels/TREX2Base/best.pt')
device = select_device('0') # 0 for gpu, '' for cpu
# initialize deepsort
cfg = get_config()
cfg.merge_from_file("deep_sort/configs/deep_sort.yaml")
deepsort = DeepSort('osnet_x0_25',
                    device,
                    max_dist=cfg.DEEPSORT.MAX_DIST,
                    max_iou_distance=cfg.DEEPSORT.MAX_IOU_DISTANCE,
                    max_age=cfg.DEEPSORT.MAX_AGE, n_init=cfg.DEEPSORT.N_INIT, nn_budget=cfg.DEEPSORT.NN_BUDGET,
                    )
# Get names and colors
names = model.module.names if hasattr(model, 'module') else model.names

from yolov5 import detect
from multiprocessing import Process
from threading import Thread

source ="RocketLunch1.mp4"


cap = cv2.VideoCapture(source)

def stream():
    cap = cv2.VideoCapture(source)
    model.iou=0.5
    model.conf=0.15
    #cap = cv2.VideoCapture(source)
    while (cap.isOpened()):
        ret, frame = cap.read()
        if not ret:
            print("Error: failed to capture image")
            break
        print("inside stream")
        results = model(frame,augment=False,size=640)
        for i in results.render():
            data=im.fromarray(i)
            data.save('demo.jpg')

        annotator = Annotator(frame, line_width=2, pil=not ascii)

        im0 = annotator.result()
        image_bytes = cv2.imencode('.jpg', im0)[1].tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n')
    cap.release()
    cv2.destroyAllWindows()
                    
                            

def detection():
    model.conf = 0.15
    model.iou = 0.5
    num=0.01
    while (cap.isOpened()):
        ret,frame = cap.read()
        if not ret:
            print("Erorr:faild to capture image")
            break
        results = model(frame, augment=True,size=640)   
        pred = results.pandas().xyxy[0]
        print("inside detection")
        for index, row in pred.iterrows():
            print(row['class'], row['confidence'])
            detection=float(row['confidence'])
            if str(row['class']) == "0":
                print("Lunch")
            if float(row['confidence']) > 0.15:
                print("detection",detection)
                return(detection)
            return num
    cap.release()
    cv2.destroyAllWindows()







if __name__ == '__main__':
    Thread(target = stream).start()
    Thread(target = detection).start()
# if __name__ == '__main__':
#     p1 = Process(target = stream)
#     p2 = Process(target = detection)

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()      

def video_feed(request):
    return StreamingHttpResponse(stream(), content_type='multipart/x-mixed-replace; boundary=frame')   

def detection_percentage(request):
    return HttpResponse(detection())






# def detection():
#     model.conf = 0.1
#     model.iou = 0.5
#     while (cap.isOpened()):
#         ret,frame = cap.read()
#         if not ret:
#             print("Erorr:faild to capture image")
#             break
#         results = model(frame, augment=True,size=640)   
                  
#         det = results.pred[0]
#         # if det is not None and len(det):
#         #     xywhs = xyxy2xywh(det[:, 0:4])
#         #     confs = det[:, 4]
#         #     clss = det[:, 5]
#         #     outputs = deepsort.update(xywhs.cpu(), confs.cpu(), clss.cpu(), frame)

#         #     for j, (output, conf) in enumerate(zip(outputs, confs)):
#         #             label = f'{conf:.2f}'
#         #             return("s",label)
#         # det = results.pred[0]
#         # pred = results.pandas().xyxy[0]
#         # if det is not None and len(det):
#         #     xywhs = xyxy2xywh(det[:, 0:4])
#         #     confs = det[:, 4]
#         #     clss = det[:, 5]
#         #     outputs = deepsort.update(xywhs.cpu(), confs.cpu(), clss.cpu(), frame)

#         #     for j, (output, conf) in enumerate(zip(outputs, confs)):
#         #             label = f'{conf:.2f}'
#         #             return(label)
#         pred = results.pandas().xyxy[0]
#         for index, row in pred.iterrows():
#             print(row['class'], row['confidence'])
#             detection=float(row['confidence'])
#             if str(row['class']) == "0":
#                 print("Lunch")
#             if float(row['confidence']) > 0.01:
#                 print("detection",detection)
#                 return(detection)
#     cap.release()
#     cv2.destroyAllWindows()
















# from django.shortcuts import render
# from django.http import StreamingHttpResponse,HttpResponse
# import yolov5,torch
# from yolov5.utils.general import (check_img_size, non_max_suppression, scale_coords, 
#                                   check_imshow, xyxy2xywh, increment_path)
# from yolov5.utils.torch_utils import select_device, time_sync
# from yolov5.utils.plots import Annotator, colors
# from deep_sort.utils.parser import get_config
# from deep_sort.deep_sort import DeepSort
# import cv2
# from PIL import Image as im
# # Create your views here
# import logging
# # .
# def index(request):
#     return render(request,'index.html')

# print(torch.cuda.is_available())
# #load model
# #model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
# model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:/Users/ilaya/trainningModels/TREX2Base/best.pt')
# device = select_device('0') # 0 for gpu, '' for cpu
# # initialize deepsort
# cfg = get_config()
# cfg.merge_from_file("deep_sort/configs/deep_sort.yaml")
# deepsort = DeepSort('osnet_x0_25',
#                     device,
#                     max_dist=cfg.DEEPSORT.MAX_DIST,
#                     max_iou_distance=cfg.DEEPSORT.MAX_IOU_DISTANCE,
#                     max_age=cfg.DEEPSORT.MAX_AGE, n_init=cfg.DEEPSORT.N_INIT, nn_budget=cfg.DEEPSORT.NN_BUDGET,
#                     )
# # Get names and colors
# names = model.module.names if hasattr(model, 'module') else model.names

# from yolov5 import detect
# from multiprocessing import Process
# from threading import Thread

# source ="RocketLunch1.mp4"


# cap = cv2.VideoCapture(source)

# def read_frame():
#     global has_frame
#     global frame

#     while running:
#         has_frame, frame = cap.read()
#         #time.sleep(.1)  # 0.1s to use less CPU

# def stream():
#     cap = cv2.VideoCapture(source)
#     model.iou=0.5
#     model.conf=0.1
#     #cap = cv2.VideoCapture(source)
#     while (cap.isOpened()):
#         ret, frame = cap.read()
#         if not ret:
#             print("Error: failed to capture image")
#             break
#         print("inside stream")
#         results = model(frame,augment=False,size=640)
#         for i in results.render():
#             data=im.fromarray(i)
#             data.save('demo.jpg')

      
#         annotator = Annotator(frame, line_width=2, pil=not ascii)

#         im0 = annotator.result()
#         image_bytes = cv2.imencode('.jpg', im0)[1].tobytes()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n')
#     cap.release()
#     cv2.destroyAllWindows()
                    
# def details():
#      ret,frame = cap.read()
#      results=model(frame,augment=True)
#      labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1].numpy()
#      det = results.pred[0]
#      for *xyxy, conf, cls in det:
#            num=torch.IntTensor.item(conf)
#            floatNum=torch.IntTensor.item(conf)
#            return floatNum
#         #    num=f"{floatNum:.2f}"
#         #    numFloaf = float(num)
#         #    re
                                       

# def detection():
#     model.conf = 0.1
#     model.iou = 0.5

#     while (cap.isOpened()):
#         ret,frame = cap.read()
#         if not ret:
#             print("Erorr:faild to capture image")
#             break
#         results = model(frame, augment=True,size=640)   
#         pred = results.pandas().xyxy[0]
#         print("inside detection")
#         for index, row in pred.iterrows():
#             print(row['class'], row['confidence'])
#             detection=float(row['confidence'])
#             if str(row['class']) == "0":
#                 print("Lunch")
#             if float(row['confidence']) > 0.1:
#                 print("detection",detection)
#                 return(detection)
#             else:
#                 return None
#     cap.release()
#     cv2.destroyAllWindows()

# # def next_frame():
# # if __name__ == '__main__':
# #     Thread(target = stream).start()
# #     Thread(target = detection).start()
# if __name__ == '__main__':
#     p1 = Process(target = stream)
#     p1.start()
#     p2 = Process(target = detection)
#     p2.start()
#     p1.join()
#     p2.join()      

# def video_feed(request):
#     return StreamingHttpResponse(stream(), content_type='multipart/x-mixed-replace; boundary=frame')   

# def detection_percentage(request):
#     return HttpResponse(detection())






# def detection():
#     model.conf = 0.1
#     model.iou = 0.5
#     while (cap.isOpened()):
#         ret,frame = cap.read()
#         if not ret:
#             print("Erorr:faild to capture image")
#             break
#         results = model(frame, augment=True,size=640)   
                  
#         det = results.pred[0]
#         # if det is not None and len(det):
#         #     xywhs = xyxy2xywh(det[:, 0:4])
#         #     confs = det[:, 4]
#         #     clss = det[:, 5]
#         #     outputs = deepsort.update(xywhs.cpu(), confs.cpu(), clss.cpu(), frame)

#         #     for j, (output, conf) in enumerate(zip(outputs, confs)):
#         #             label = f'{conf:.2f}'
#         #             return("s",label)
#         # det = results.pred[0]
#         # pred = results.pandas().xyxy[0]
#         # if det is not None and len(det):
#         #     xywhs = xyxy2xywh(det[:, 0:4])
#         #     confs = det[:, 4]
#         #     clss = det[:, 5]
#         #     outputs = deepsort.update(xywhs.cpu(), confs.cpu(), clss.cpu(), frame)

#         #     for j, (output, conf) in enumerate(zip(outputs, confs)):
#         #             label = f'{conf:.2f}'
#         #             return(label)
#         pred = results.pandas().xyxy[0]
#         for index, row in pred.iterrows():
#             print(row['class'], row['confidence'])
#             detection=float(row['confidence'])
#             if str(row['class']) == "0":
#                 print("Lunch")
#             if float(row['confidence']) > 0.01:
#                 print("detection",detection)
#                 return(detection)
#     cap.release()
#     cv2.destroyAllWindows()












# from django.shortcuts import render
# from django.http import StreamingHttpResponse,HttpResponse
# import yolov5,torch
# from yolov5.utils.general import (check_img_size, non_max_suppression, scale_coords, 
#                                   check_imshow, xyxy2xywh, increment_path)
# from yolov5.utils.torch_utils import select_device, time_sync
# from yolov5.utils.plots import Annotator, colors
# from deep_sort.utils.parser import get_config
# from deep_sort.deep_sort import DeepSort
# import cv2
# from PIL import Image as im
# # Create your views here
# import logging
# # .
# def index(request):
#     return render(request,'index.html')

# print(torch.cuda.is_available())
# #load model
# #model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
# model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:/Users/ilaya/trainningModels/TREX2Base/best.pt')
# device = select_device('0') # 0 for gpu, '' for cpu
# # initialize deepsort
# cfg = get_config()
# cfg.merge_from_file("deep_sort/configs/deep_sort.yaml")
# deepsort = DeepSort('osnet_x0_25',
#                     device,
#                     max_dist=cfg.DEEPSORT.MAX_DIST,
#                     max_iou_distance=cfg.DEEPSORT.MAX_IOU_DISTANCE,
#                     max_age=cfg.DEEPSORT.MAX_AGE, n_init=cfg.DEEPSORT.N_INIT, nn_budget=cfg.DEEPSORT.NN_BUDGET,
#                     )
# # Get names and colors
# names = model.module.names if hasattr(model, 'module') else model.names
# import threading
# from yolov5 import detect
# from multiprocessing import Process
# from threading import Thread
# import time
# source ="RocketLunch1.mp4"




# def read_frame():
#     global has_frame
#     global frame

#     while running:
#         has_frame, frame = cap.read()
#         #time.sleep(.1)  # 0.1s to use less CPU

# def stream():
#     global frame1
#     while (running):
#         if not has_frame:
#             print("Error: failed to capture image")
#             break     
#         print("inside stream")
#         frame1=frame.copy()
#         results = model(frame1,augment=False,size=640)
#         for i in results.render():
#             data=im.fromarray(i)
#             data.save('demo.jpg')
#         annotator = Annotator(frame1, line_width=2, pil=not ascii)
#         im0 = annotator.result()
#         image_bytes = cv2.imencode('.jpg', im0)[1].tobytes()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n')
#     cv2.destroyAllWindows()
#     cap.release()
                    
# def details():
#     global frame2
#     while running:
#         if not has_frame:
#             print("Error: failed to capture image")
#             break 
#         frame2 = frame.copy()
    
#         results=model(frame2,augment=True)
#         labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1].numpy()
#         det = results.pred[0]
#         for *xyxy, conf, cls in det:
#            num=torch.IntTensor.item(conf)
#            floatNum=torch.IntTensor.item(conf)
#            return floatNum
        
                                       

# def detection():
#     global frame2
#     while (running):
#         ret,frame = cap.read()
#         if not has_frame:
#             print("Erorr:faild to capture image")
#             break
#         frame2 = frame.copy()
#         results = model(frame2, augment=True,size=640)   
#         pred = results.pandas().xyxy[0]
#         print("inside detection")
#         for index, row in pred.iterrows():
#             print(row['class'], row['confidence'])
#             detection=float(row['confidence'])
#             if str(row['class']) == "0":
#                 print("Lunch")
#             if float(row['confidence']) > 0.1:
#                 print("detection",detection)
#                 return(detection)
#             time.sleep(.1)
            
#     cv2.destroyAllWindows()
#     cap.release()
        

# has_frame = False 
# frame = None   # original frame from camera

# frame1 = None  # frame after processing
# frame2 = None  # frame after processing
# cap = cv2.VideoCapture(source)
# t0 = threading.Thread(target=read_frame)
# t1 = threading.Thread(target=stream)
# t2 = threading.Thread(target=detection)
# running = True
# t0.start()
# t1.start()
# t2.start()


# running = False

# t0.join()
# t1.join()
# t2.join()

# while cv2.waitKey(100) != 27:  # ESC  # 100ms to use less CPU

#     if frame1 is not None:
#         cv2.imshow('Capturing1', frame1)

#     if frame2 is not None:
#         cv2.imshow('Capturing2', frame2)

# def video_feed(request):
#     return StreamingHttpResponse(stream(), content_type='multipart/x-mixed-replace; boundary=frame')   

# def detection_percentage(request):
#     return HttpResponse(detection())


# def next_frame():
# if __name__ == '__main__':
#     Thread(target = stream).start()
#     Thread(target = detection).start()
# if __name__ == '__main__':
#     p1 = Process(target = stream)
#     p1.start()
#     p2 = Process(target = detection)
#     p2.start()
#     p1.join()
#     p2.join()      







# def detection():
#     model.conf = 0.1
#     model.iou = 0.5
#     while (cap.isOpened()):
#         ret,frame = cap.read()
#         if not ret:
#             print("Erorr:faild to capture image")
#             break
#         results = model(frame, augment=True,size=640)   
                  
#         det = results.pred[0]
#         # if det is not None and len(det):
#         #     xywhs = xyxy2xywh(det[:, 0:4])
#         #     confs = det[:, 4]
#         #     clss = det[:, 5]
#         #     outputs = deepsort.update(xywhs.cpu(), confs.cpu(), clss.cpu(), frame)

#         #     for j, (output, conf) in enumerate(zip(outputs, confs)):
#         #             label = f'{conf:.2f}'
#         #             return("s",label)
#         # det = results.pred[0]
#         # pred = results.pandas().xyxy[0]
#         # if det is not None and len(det):
#         #     xywhs = xyxy2xywh(det[:, 0:4])
#         #     confs = det[:, 4]
#         #     clss = det[:, 5]
#         #     outputs = deepsort.update(xywhs.cpu(), confs.cpu(), clss.cpu(), frame)

#         #     for j, (output, conf) in enumerate(zip(outputs, confs)):
#         #             label = f'{conf:.2f}'
#         #             return(label)
#         pred = results.pandas().xyxy[0]
#         for index, row in pred.iterrows():
#             print(row['class'], row['confidence'])
#             detection=float(row['confidence'])
#             if str(row['class']) == "0":
#                 print("Lunch")
#             if float(row['confidence']) > 0.01:
#                 print("detection",detection)
#                 return(detection)
#     cap.release()
#     cv2.destroyAllWindows()














# def stream():
#     model.iou = 0.5
#     model.conf=0.25
#     while(cap.isOpened()):
#         ret, frame = cap.read()
#         if not ret:
#             print("Error: failed to capture image")
#             break

#         results = model(frame, augment=True)
#         # proccess
#         annotator = Annotator(frame, line_width=2, pil=not ascii) 
#         det = results.pred[0]
#         if det is not None and len(det):   
#             xywhs = xyxy2xywh(det[:, 0:4])
#             confs = det[:, 4]
#             clss = det[:, 5]
#             outputs = deepsort.update(xywhs.cpu(), confs.cpu(), clss.cpu(), frame)
#             if len(outputs) > 0:   
#                 for j, (output, conf) in enumerate(zip(outputs, confs)):

#                     bboxes = output[0:4]
#                     id = output[4]
#                     cls = output[5]

#                     c = int(cls)  # integer class
#                     label = f'{conf:.2f}'
#                     annotator.box_label(bboxes, label, color=colors(c, True))

#         im0 = annotator.result()    
#         image_bytes = cv2.imencode('.jpg', im0)[1].tobytes()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n')  
#     cap.release()
#     cv2.destroyAllWindows()





# flag=True
# def detection():
#     if(cap.isOpened()):
#         ret,frame = cap.read()
#         if ret:
#             results = model(frame, augment=False,size=640)  
#             pred = results.pandas().xyxy[0]
#             for index, row in pred.iterrows():
#                 if float(row['confidence']) > 0.15:
#                     detection=float(row['confidence'])
#                     data={"det":detection,"isRunning":cap.isOpened()}
#                     dataJson=json.dumps(data)
#                     return dataJson
#             dataCap={"isRunning":cap.isOpened()}
#             dataJsonCap=json.dumps(dataCap)               
#             return dataJsonCap
#         dataCap={"isRunning":cap.isOpened()}
#         dataJsonCap=json.dumps(dataCap)               
#         return dataJsonCap
#     dataCap={"isRunning":cap.isOpened()}
#     dataJsonCap=json.dumps(dataCap)               
#     return dataJsonCap
   
#cap2 = cv2.VideoCapture(source2)


# def select_frames(total_frames, num_frames, fps, *args):
#     """This function will return the indices of the frames to be captured"""
#     N = 1
#     t = np.arange(total_frames)
#     f = np.arange(num_frames)
#     mask = np.resize(f, total_frames)

#     return t[mask < N][:num_frames].tolist()

# # Let's assume that the duration of your video is 120 seconds
# # and you want 1 frame for each second 
# # (therefore, setting `num_frames` to 120)
# reader = Videos(num_frames=122, mode=select_frames)

# video = reader.read("LaunchC2.mp4")  # A video tensor/array

























#20.11
# cap = cv2.VideoCapture("RocketLunch11.mp4")
# cap.set(3,640) # set Width
# cap.set(4,480) # set Height

# def stream():
#     cap = cv2.VideoCapture("RocketLunch11.mp4")
#     cap.set(3,640) # set Width
#     cap.set(4,480) # set Height
#     fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
#     out = cv2.VideoWriter('output.avi',fourcc, 20.0,(int(cap.get(3)),int(cap.get(4))))
#     #out = cv2.VideoWriter('output.avi',fourcc, 20.0,(int(cap.get(3)),int(cap.get(4))))
#     model.iou=0.5
#     while (cap.isOpened()):
#         ret, frame = cap.read()
        
#         # cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         if not ret:
#             print("Error: failed to capture image")
#             break
#         results = model(frame,augment=False,size=640)
#         for i in results.render(): 
            
#             data=im.fromarray(i)
#             # data.save('demo.jpg') 
#         out.write(frame)      
#         annotator = Annotator(frame, line_width=2, pil=not ascii)
#         #cv2.imshow('Frame',frame)
#         im0 = annotator.result()
#         #print(results)
#         # results.save(save_dir='data/output/images') 
#         image_bytes = cv2.imencode('.jpg', im0)[1].tobytes()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n') 
#     cap.release()
#     out.release()
#     cv2.destroyAllWindows()



# def detection():
#         if(cap.isOpened()):
#             ret,frame = cap.read()
#             if not ret:                
#                 data={"isRunning":False}
#                 dataJson=json.dumps(data)
#                 print("in not ret")
#                 return dataJson
#             results = model(frame,augment=False,size=640) 
#             pred = results.pandas().xyxy[0]
#             for index, row in pred.iterrows():
#                 if float(row['confidence']) > 0.15:
#                     print("in if")
#                     detection=float(row['confidence'])
#                     det = '%.2f' % detection
#                     data={"det":det,"isRunning":cap.isOpened()}
#                     dataJson=json.dumps(data)
#                     return dataJson
#             data={"isRunning":cap.isOpened()}
#             dataJson=json.dumps(data)               
#             return dataJson
          
#         data={"isRunning":False}
#         dataJson=json.dumps(data)              
#         return dataJson
        


# def video_feed(request):
#     return StreamingHttpResponse(stream(), content_type='multipart/x-mixed-replace; boundary=frame')   

# def detection_percentage(request):
#     return HttpResponse(detection())














# from django.db import djmongodbengine
#cap = cv2.VideoCapture("RocketLunch11.mp4")
# cap.set(3,640) # set Width
# cap.set(4,480) # set Height
# seconds =  t.time()
# source="RocketLunch11.mp4"
 # saveName='result.avi'
# source = 'RocketLunch11.mp4'
# video = pafy.new(source).streams[-1]
# assert video is not None
# best  = video.getbest(preftype="webm")
# print("sotce",source)
    
    
    
    
    # Open the video file using the cv2.VideoCapture class
    # cap = cv2.VideoCapture(file)
    # video = cv2.VideoCapture(file.read())
    # success, image = video.read()

    # # Check if the video file was opened successfully
    # # if not image.isOpened():
    # #     print("Error: Could not open video file")
    # #     return HttpResponse("Error: Could not open video file", status=500)

    # # Read the first frame from the video file
    
    # success, image = video.read()
    # frame=cv2.imencode('.jpg', image)[1].tobytes()

    # # Check if the first frame was read successfully
    # if not success:
    #     print("Error: Could not read first frame from video file")
    #     return HttpResponse("Error: Could not read first frame from video file", status=500)

    # # Return the first frame as an image
    # return HttpResponse(frame, content_type="image/jpeg")
    # if request.method == 'GET':
    #     global filename
    #     filename = request.GET.get('filename','notFile')
    #     # db = mongo_connection()
    #     storage = GridFSStorage()
    #      # Create a new instance of the GridFSStorage class
    #     db = mongo_connection()
    #     #fs = GridFSStorage()

    #      # Open the video file using the `open()` method and specify the collection where the file is stored
    #     with storage.open(filename, 'rb') as video_file:
    #     # Use the `Image` class from the Pillow library to open the video file as an image
    #     # This allows us to extract the first frame from the video
    #         img = Image.open(video_file)
    #         # Use the `seek()` method to move to the first frame of the video
    #         img.seek(0)

    #         # Use the `save()` method to save the first frame as an image file
    #         # We save the frame to a BytesIO object in memory instead of to a file on disk
    #         img_buffer = BytesIO()
    #         img.save(img_buffer, format='JPEG')
    #         img_buffer.seek(0)

    #         # Create a new `HttpResponse` object using the image data in the BytesIO object
    #         response = HttpResponse(img_buffer.read(), content_type="image/jpeg")
    #         return response
    




# video_name_db=video_name+str('.mp4')
# # file_location_db= url
#fps = cap.get(cv2.CAP_PROP_FPS)
#out = cv2.VideoWriter('output.avi',fourcc, 20.0,(int(cap.get(3)),int(cap.get(4))))
#model.iou=0.5
# print("saveName",saveName)
# path_uplode_video_withDetrction = path_uplode_video_withDetrction + str('.mp4')
# file_loc=path_uplode_video_withDetrction
#save_name_edit = saveName.replace('.mp4','')
#file_loc ="C:/Users/ilaya/LaunchVideos/VideoBefor/MissileLaunch1"

 #     metadata = db.fs.files.find_one({"_id": file_id}, {"metadata": 1})
# # Get the image data from the metadata
#     print(metadata["metadata"]["author"])  # Output: "John Smith"
    #image_data = metadata["metadata"]["image"]
    # file_id = '6398a40762c697ce4acfd8ff'

    # # file=fs.find_one({"_id": file_id})
    # metadata = {
    #     "_contentType": "application/pdf",
    #     "_class": "com.mongodb.BasicDBObject"
    # }
    # # Open the image file
    # newvalues = { "$set": { 'quantity': 25 } }
    # # with open("C:/Users/ilaya/upload.jpeg", 'rb') as f:
    # #     image_data = f.read()
    # collection.update_one({'_id': file_id}, {'$set': newvalues})
        #db.fs.files.replace_one({'filename': 'ResultOfVideo_MissileLaunch3.mp4'}, {'$set': {'metadata': image_data}})
        #db.fs.VideosDetection.files.replace_one({'filename': 'ResultOfVideo_MissileLaunch3.mp4'}, {'$set': {'metadata': image_data}})
        #fs.update({'filename': 'ResultOfVideo_MissileLaunch3.mp4'}, {'$set': {'metadata': image_data}})
        #db.fs.save(file)
        # fs.put({'image': image_data}, filename=file)
    # Add the image data as metadata to the existing file
        # file.metadata['image'] = image_data
        # fs.put(file, filename='ResultOfVideo_MissileLaunch3.mp4')
    # Open the image file.
  
    # if(image_data):
    #     print("Image")

    # # Add the image data as metadata to the existing file
    # file.metadata[resource] = ContentFile(image_data)

    # fs.put(file, filename='ResultOfVideo_MissileLaunch3.mp4')




# def save(request):
#     fileNmae="ResultOfVideo_MissileLaunch3.mp4"
#     client=mongo_connection()
#     bucket = GridFSBucket(client)
#     file = bucket.find({ 'filename': fileNmae })

# # Use the `open_download_stream` method to create a readable stream for the file
#     stream = bucket.open_download_stream(file._id)

# # Use the stream to read the file contents
#     for chunk in stream:
#     # Process the file data
#     # In this example, we save the data to a new file
#         with open('/path/to/new/file', 'wb') as f:
#             f.write(chunk)


# def video_id(url):
#     if url.startswith(('youtu','www')):
#         url = 'http://' + url

#     query = urlparse(url)

#     if 'youtube' in query.hostname:
#         if query.path == '/watch':
#             return parse_qs(query.query)['v'][0]
#         elif query.path.startswith(('/embed','/v/')):
#             return query.path.split('/')[2]
#     elif 'youtube.be' in query.hostname:
#         return query.path[1:]
#     else:
#         raise ValueError


# url=video_id(content)
# play = pafy.new(self._URL).streams[-1]
# body_unicode=request.body.decode('utf-8') 
# body=json.loads(body_unicode)
# content=body['url']


# def write_video(file_path, frames, fps):
#     """
#     Writes frames to an mp4 video file
#     :param file_path: Path to output video, must end with .mp4
#     :param frames: List of PIL.Image objects
#     :param fps: Desired frame rate
#     """

#     w, h = frames[0].size
#     fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
#     writer = cv2.VideoWriter(file_path, fourcc, fps, (w, h))

#     for frame in frames:
#         writer.write(pil_to_cv(frame))

#     writer.release() 

# def saveVideo():
# # Stream results
#             im0 = annotator.result()
#             if show_vid:
#                 cv2.imshow(str(p), im0)
#                 if cv2.waitKey(1) == ord('q'):  # q to quit
#                     raise StopIteration

#             # Save results (image with detections)
#             if save_vid:
#                 if vid_path != save_path:  # new video
#                     vid_path = save_path
#                     if isinstance(vid_writer, cv2.VideoWriter):
#                         vid_writer.release()  # release previous video writer
#                     if vid_cap:  # video
#                         fps = vid_cap.get(cv2.CAP_PROP_FPS)
#                         w = int(vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#                         h = int(vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#                     else:  # stream
#                         fps, w, h = 30, im0.shape[1], im0.shape[0]

#                     vid_writer = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))
#                 vid_writer.write(im0)


# if __name__ == '__main__':
#     Thread(target = stream).start()
#     Thread(target = detection).start()

# if __name__ == '__main__':
#     p1= Process(target = stream)
#     p2= Process(target = detection)
#     p1.start() 
#     p2.start()

#     p1.join()
#     p2.join()    



    
# def SaveImage():
#     while (cap.isOpened()):
#         ret, frame = cap.read()
#         if not ret:
#             print("Error: failed to capture image")
#             break
#         results = model(frame,augment=False,size=640)
#         for i in results.render():
#             data=im.fromarray(i)
#             data.save('demo.jpg') 
#         annotator = Annotator(frame, line_width=2, pil=not ascii)
#         im0 = annotator.result()
#         _, im_arr = cv2.imencode('.jpg', im0)
# 	    im_b64 = base64.b64encode(im_arr.tobytes()).decode('utf-8')
# 	    return im_b64

# def results_to_json(results, model):
# 	''' Converts yolo model output to json (list of list of dicts)'''
# 	return [
# 				[
# 					{
# 					"class": int(pred[5]),
# 					"class_name": model.model.names[int(pred[5])],
# 					"bbox": [int(x) for x in pred[:4].tolist()], #convert bbox results to int from float
# 					"confidence": float(pred[4]),
# 					}
# 				for pred in result
# 				]
# 			for result in results.xyxy
# 			]


# def detection():
#     model.conf = 0.1
#     model.iou = 0.5
#     while (cap.isOpened()):
#         ret,frame = cap.read()
#         if not ret:
#             print("Erorr:faild to capture image")
#             break
#         results = model(frame, augment=True,size=640)   
                  
#         det = results.pred[0]
#         # if det is not None and len(det):
#         #     xywhs = xyxy2xywh(det[:, 0:4])
#         #     confs = det[:, 4]
#         #     clss = det[:, 5]
#         #     outputs = deepsort.update(xywhs.cpu(), confs.cpu(), clss.cpu(), frame)

#         #     for j, (output, conf) in enumerate(zip(outputs, confs)):
#         #             label = f'{conf:.2f}'
#         #             return("s",label)
#         # det = results.pred[0]
#         # pred = results.pandas().xyxy[0]
#         # if det is not None and len(det):
#         #     xywhs = xyxy2xywh(det[:, 0:4])
#         #     confs = det[:, 4]
#         #     clss = det[:, 5]
#         #     outputs = deepsort.update(xywhs.cpu(), confs.cpu(), clss.cpu(), frame)

#         #     for j, (output, conf) in enumerate(zip(outputs, confs)):
#         #             label = f'{conf:.2f}'
#         #             return(label)
#         pred = results.pandas().xyxy[0]
#         for index, row in pred.iterrows():
#             print(row['class'], row['confidence'])
#             detection=float(row['confidence'])
#             if str(row['class']) == "0":
#                 print("Lunch")
#             if float(row['confidence']) > 0.01:
#                 print("detection",detection)
#                 return(detection)
#     cap.release()
#     cv2.destroyAllWindows()



##############################################################
#6.12#
##############################################################
# startvideo =False
# confidence = None
# check = True
# end=True
# time_to_detect=0
# det=0
# start =  timer.time()



# def stream(source):
#     if startvideo : 
#         saveName = str('ResultOfVideo_') + str(source) + str('.avi')
#         source=content
#         url = source + str('.mp4')
#         print("Source",source)
#         cap = cv2.VideoCapture(url)
#         imageWidth = int(cap.get(3))
#         imageHeight = int(cap.get(4))
#         model.conf=0.15
#         fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
#     #fps = cap.get(cv2.CAP_PROP_FPS)
#     # out = cv2.VideoWriter(saveName,fourcc, 8.0,(imageWidth, imageHeight))
#     #out = cv2.VideoWriter('output.avi',fourcc, 20.0,(int(cap.get(3)),int(cap.get(4))))
#     #model.iou=0.5
#         global check
#         global confidence
#         global time_to_detect
#         global det
#         while (cap.isOpened()):
#             ret, frame = cap.read()
#             print("source",source)
#             check = True
#             if not ret:
#                 print("Error: failed to capture image")
#                 check = False
#                  # print(str('Completed video ') + str(saveName))
#                 break
#             results = model(frame,augment=False,size=640)
#             # frame= cv2.resize(frame,(1200,700))
#             det = results.pred[0]
#             results.render()
#             for *xyxy, conf, cls in det:
#                 floatNum=torch.IntTensor.item(conf)
#                 num=f"{floatNum:.2f}"
#                 detection_conf = float(num)
#                 confidence = detection_conf
#                 end = timer.time()
#                 time_to_detect = end-start
#             annotator = Annotator(frame, line_width=2, pil=not ascii)
#             im0 = annotator.result()
#             image_bytes = cv2.imencode('.jpg', im0)[1].tobytes()
#             yield (b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n') 
#         # out.write(frame)      
#         cap.release()
#         # out.release()
#         cv2.destroyAllWindows()


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
    
# def detections_data():
#     end=True
#     if(confidence is not None  and len(det) > 0): 
#         final_json=[{"detection":confidence,"passtime":time_to_detect}]
#         dataJsonFinal=json.dumps(final_json)
#     if end is False:
#         return dataJsonFinal

# def video_id(url):
#     if url.startswith(('youtu','www')):
#         url = 'http://' + url

#     query = urlparse(url)

#     if 'youtube' in query.hostname:
#         if query.path == '/watch':
#             return parse_qs(query.query)['v'][0]
#         elif query.path.startswith(('/embed','/v/')):
#             return query.path.split('/')[2]
#     elif 'youtube.be' in query.hostname:
#         return query.path[1:]
#     else:
#         raise ValueError
         

# @csrf_exempt
# def video_feed(request):
#     if request.method == 'POST':
#         global content
#         global start
#         content = request.GET.get('url','not')
#         print(content)

#     return StreamingHttpResponse(stream(content), content_type='multipart/x-mixed-replace; boundary=frame')   

# def detection_percentage(request):
#     global startvideo
#     startvideo=True
#     return HttpResponse(detection())

# def data(request):
#     return HttpResponse(detections_data())








# #3.1

# def index(request):
#     return render(request,'index.html')

# print(torch.cuda.is_available())
# #load model
# #model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
# model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:/Users/ilaya/trainningModels/TREX2Base/best.pt')
# device = select_device('0') # 0 for gpu, '' for cpu
# # initialize deepsort
# cfg = get_config()
# cfg.merge_from_file("deep_sort/configs/deep_sort.yaml")
# deepsort = DeepSort('osnet_x0_25',
#                     device,
#                     max_dist=cfg.DEEPSORT.MAX_DIST,
#                     max_iou_distance=cfg.DEEPSORT.MAX_IOU_DISTANCE,
#                     max_age=cfg.DEEPSORT.MAX_AGE, n_init=cfg.DEEPSORT.N_INIT, nn_budget=cfg.DEEPSORT.NN_BUDGET,
#                     )
# # Get names and colors
# names = model.module.names if hasattr(model, 'module') else model.names


# startvideo = False
# confidence = None
# check = True
# end=True
# det=0
# start =  timer.time()
# previous_time_fps= None

# MIN_FPS = 1.0
# MAX_FPS = 60.0

# connect_str = "mongodb+srv://ilay:asis2003@cluster0.2mtny9z.mongodb.net/?retryWrites=true&w=majority"
# client = pymongo.MongoClient("mongodb+srv://ilay:asis2003@cluster0.2mtny9z.mongodb.net/?retryWrites=true&w=majority")
# connect = MongoClient(connect_str) 

# def mongo_connection():
#     connect_str = "mongodb+srv://ilay:asis2003@cluster0.2mtny9z.mongodb.net/?retryWrites=true&w=majority"
#     try:
#         connect = MongoClient(connect_str)
#         print("Connect Succeed !",connect)
#         return connect.Rocket
#     except Exception as err:
#         print("Error connecting" + Exception)

# def stream(source):
#     end = False
#     detection_data = []
#     if startvideo : 
#         global file_loc,file_name,fs,check,confidence,time_to_detect,det,previous_time_fps
#         source=content
#         locationvideo = content.split("/")
#         video_name=locationvideo[-1]
#         print("Source1",source)
#         print("video_name",video_name)
#         url = source + str('.mp4')
#         saveName = str('ResultOfVideo_') +str(video_name) + str('.mp4')
#         saveNameJson =  str('ResultOfVideo_') +str(video_name)
#         file_name=saveName
#         cap = cv2.VideoCapture(url)
#         imageWidth = int(cap.get(3))
#         imageHeight = int(cap.get(4))
#         print("url:",url)
       
#         path_to_save_video = "C:/Users/ilaya/LaunchVideos/VideoAfter/"
#         path_uplode_video_withDetrction = (path_to_save_video) + (saveName)
#         print("path_uplode_video_withDetrction",path_uplode_video_withDetrction)
#         print("path_uplode_video_withDetrction",path_uplode_video_withDetrction)
#         laoction_name = path_to_save_video + saveName
#         file_loc=laoction_name

#         fps = cap.get(cv2.CAP_PROP_FPS)
#         fourcc = cv2.VideoWriter_fourcc(*'VIDX')
#         out = cv2.VideoWriter(laoction_name,fourcc, 8.0,(imageWidth, imageHeight))
#         print("laoction_name",laoction_name)
#         print("url",url)
#         model.conf=0.15
#         while (cap.isOpened()):
#             check = True
#             ret, frame = cap.read()
#             if not ret:
#                 print("Error: failed to capture image")
#                 check = False
#                 #print(str('Completed video ') + str(saveName))
#                 break
#             results = model(frame,augment=False,size=640)
#             # frame= cv2.resize(frame,(1200,700))
#             current_time_fps = timer.perf_counter_ns()
            
#             framespersecond= int(cap.get(cv2.CAP_PROP_FPS))
#             print("framespersecond",framespersecond)
#             # if previous_time_fps is not None:
#             #     fps = 1 / ((current_time_fps - previous_time_fps) / 1000000000)
#             #     # if fps < MIN_FPS:
#             #     #    fps = MIN_FPS
#             #     # elif fps > MAX_FPS:
#             #     #     fps = MAX_FPS
#             #     # print("fps" , fps )
                
#             #     out.set(cv2.CAP_PROP_FPS, fps)
               
#             #     # out.set(cv2.CAP_PROP_FPS, fps)
#             #     #
#             #     # timer.sleep(1.0 / fps)
#             results.render()
#             out.write(frame)
#             previous_time_fps = current_time_fps
           
            
           
#             det = results.pred[0]
#             for *xyxy, conf, cls in det:
#                 # confidence = conf.item()
#                 # print("confidenceJson",confidenceJson)
#                 floatNum=torch.IntTensor.item(conf)
#                 num=f"{floatNum:.2f}"
#                 detection_conf = float(num)
#                 confidence = detection_conf
#                 path_to_frame =  "C:/Users/ilaya/LaunchVideos/Frame/BestFrameFor" +  str(saveName) + ".jpg"
#                 if confidence > 0.6:
#                     cv2.imwrite(path_to_frame,frame)
#                 end = timer.time()
#                 time_to_detect = end-start
#                 t= 0
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

#             annotator = Annotator(frame, line_width=2, pil=not ascii)
#             im0 = annotator.result()
#             image_bytes = cv2.imencode('.jpg', im0)[1].tobytes()
#             yield (b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n') 
#         cap.release()
#         out.release()
#         cv2.destroyAllWindows()
#         end = True
#         json_file_name = "detection_data_" + str(saveNameJson)+str(".json")
#         with open(json_file_name, "w") as f:
#             json.dump(detection_data, f)
#         print("json_file_name",json_file_name)
#         print("file_loc at end",file_loc,"filename",file_name)
#     if end:
#         upload_video_file_toMongo(file_loc=file_loc,file_name=file_name,json_file=json_file_name,path_to_frame=path_to_frame)
#         # upload_video_file_toMongo(file_loc=file_loc,file_name=file_name)
#         # get_first_video_frame(path_to_frame,file_name,json_file=json_file_name)



# def upload_video_file_toMongo(file_loc,file_name,json_file,path_to_frame):
#     pathForUploadPhoto = path_to_frame
#     print("file loc at upload_video_file_toMongo",file_loc)
#     db = mongo_connection()
#     fs = gridfs.GridFS(db,collection="VideosDetection")

#     with open(file_loc,'rb') as file_data:
#         data = file_data.read()
#     with open(json_file, "r") as f:
#         json_data = json.load(f)    
#     with open(pathForUploadPhoto, "rb") as f:
#         image_data = f.read()

#     metadata = {
#         "detectionData": json_data,
#         "image": image_data
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
#         "detectionData": json_data,
#         "image": image_data
#     }
#     #metadata = db.fs.files.find_one({"_id": file_id}, {"metadata": 1})
#     # db.VideosDetection.files.update_one({"_id": file_id}, {"$set": {"metadata": metadata}})
#     update_metadata(file_id,metadata)
#     metadata = db.VideosDetection.files.find_one({"_id": file_id}, {"metadata": 1})
#     image_data = metadata["metadata"]["image"]
#     with open("image.jpg", "wb") as f:
#         f.write(image_data)
#     # Display the image using an image library such as Pillow
#     imageResult = im.open(BytesIO(image_data))
#     imageResult.show()

# def update_metadata(file_id, metadata):
#     # Connect to the MongoDB database
#     connect_str = "mongodb+srv://ilay:asis2003@cluster0.2mtny9z.mongodb.net/?retryWrites=true&w=majority"
#     client = pymongo.MongoClient(connect_str)
#     db = client["Rocket"]
#     fs = gridfs.GridFS(db, collection="VideosDetection")

#     # Update the metadata for the file with the given ID
#     try:
#         result = fs.VideosDetection.files.update_one(
#             {"_id": file_id},
#             {"$set": {"metadata": metadata}}
#         )
#         print("Metadata updated successfully")
#     except Exception as e:
#         print("Error updating metadata: ", e)

# def get_files(request):
#     # Connect to the MongoDB database
#     connect_str = "mongodb+srv://ilay:asis2003@cluster0.2mtny9z.mongodb.net/?retryWrites=true&w=majority"
#     client = pymongo.MongoClient(connect_str)
#     db = client["Rocket"]
#     fs = gridfs.GridFS(db,collection="VideosDetection")

#     # Find all the files in the database
#     files = fs.find()

#     data = []
#     # Iterate through the files and extract the metadata and filename
#     for file in files:
#         metadata = file.metadata
#         filename = file.filename
    
#         # Convert the binary data in the metadata to a base64-encoded string
#         if 'image' in metadata:
#             image_data = metadata['image']
#             metadata['image'] = base64.b64encode(image_data).decode('utf-8')

#         data.append({'filename': filename, 'metadata': metadata})

#     # Return the data as a JSON response
#     return HttpResponse(json.dumps(data), content_type='application/json')


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


# @csrf_exempt
# def video_feed(request):
#     if request.method == 'POST':
#         global content
#         global start
#         content = request.GET.get('url','not')
#         print(content)    
#     return StreamingHttpResponse(stream(content), content_type='multipart/x-mixed-replace; boundary=frame')   

# def detection_percentage(request):
#     global startvideo
#     startvideo=True
#     return HttpResponse(detection())


# def detections_data():
#     end=True
#     if(confidence is not None  and len(det) > 0): 
#         final_json=[{"detection":confidence,"passtime":time_to_detect}]
#         dataJsonFinal=json.dumps(final_json)
#     if end is False:
#         return dataJsonFinal


# @csrf_exempt
# def load_video(request):
#     if request.method == 'GET':
#         #get the fileName
#         fileName = request.GET.get('filename','FailedGetFileName')
#         #connect to db
#         connect_str = "mongodb+srv://ilay:asis2003@cluster0.2mtny9z.mongodb.net/?retryWrites=true&w=majority"
#         client = pymongo.MongoClient(connect_str)
#         db = client["Rocket"]
#         fs = gridfs.GridFS(db,collection="VideosDetection")
#         #fine the spesific file
#         file = fs.find_one({"filename": fileName})
#         if file is None:
#             return HttpResponse(status=404)
#         print("i make a response with the video file" ,fileName )

#         response = HttpResponse()
#         response['Content-Type'] = 'application/json'

#         # read the file contents into a variable
#         file_contents = file.read()
#         # encode the binary data as a base64 string
#         file_contents_base64 = base64.b64encode(file_contents).decode('utf-8')

#         detection_data = fs.find_one({"filename": fileName}).metadata['detectionData']
       

#         # convert the detection data to a JSON-formatted string
#         detection_data_json = json.dumps(detection_data)
#         print("detection_data",detection_data_json)

#         # create a dictionary with the video and detection data
#         response_data = {'video': file_contents_base64, 'detectionData': detection_data_json}


#         # return the response as JSON
#         return HttpResponse(json.dumps(response_data), content_type='application/json')








# def load_video3(request):
#     # Connect to the MongoDB database
#     db=mongo_connection()

#     # Initialize the GridFS object
#     fs= gridfs.GridFS(db,collection="VideosDetection")

#     # Get a list of all the files in the specified collection
#     files = list(fs.find())

#     # Build the response data
#     data = {
#         'files': [
#             {
#                 'id': str(file._id),
#                 'filename': file.filename,
#                 'content_type': file.content_type,
#             }
#             for file in files
#         ]
#     }

#     # Return the response as JSON
#     return JsonResponse(data)


# @require_GET
# def load_first_frame(request):

   
#     if request.method == 'GET':
#         global filename
#         filename = request.GET.get('filename','notFile')
#         db = mongo_connection()
#         fs = gridfs.GridFS(db,collection="VideosDetection")
        
#         data=db.VideosDetection.files.filename
#         print(data,"data")
#         file=data.filename
#         print(file,"file")
        

   
#     # Initialize the GridFS object
   
#     # name="ResultOfVideo_MissileLaunch3.avi"
#     # print("db.VideosDetection.files",db.VideosDetection.files.ResultOfVideo_MissileLaunch3.avi)
#     # data=db.VideosDetection.files.find_one({"file_name":name})
#     # Connect to the MongoDB instance
#     # client = MongoClient('localhost:27017')

#     # Get the database containing the video file
#     # db = client['my_database']
#     #     db = mongo_connection()
#     # # Get the GridFS instance for the database
#     #     fs = gridfs.GridFS(db,collection="VideosDetection")

#     # Get the first frame of the video file
#         first_frame = fs.get_last_version(data).read()

#     # Return the first frame as the response to the request
#         return HttpResponse(first_frame, content_type='image/jpeg')



# def get_files1(request):
#     connect_str = "mongodb+srv://ilay:asis2003@cluster0.2mtny9z.mongodb.net/?retryWrites=true&w=majority"
#     client = pymongo.MongoClient(connect_str)
#     db = client["Rocket"]
#     fs = gridfs.GridFS(db,collection="VideosDetection")
#     metadata = request.GET.get("metadata")
#     files = fs.find({"metadata": metadata})
#     if files.count() == 0:
#         return HttpResponseNotFound("No files found")
#     else:
#         # Create a zip file containing all the matching files
#         zip_buffer = BytesIO()
#         zip_file = ZipFile(zip_buffer, "w")
#         for file in files:
#             zip_file.writestr(file.filename, file.read())
#         zip_file.close()

#         # Return the zip file as a response
#         zip_buffer.seek(0)
#         response = HttpResponse(zip_buffer.read(), content_type="application/zip")
#         response["Content-Disposition"] = "attachment; filename=files.zip"
#         return response

# def get_first_video_frame2(request):
#         filename = request.GET.get("filename")
#         # Connect to the MongoDB database
#         db = mongo_connection()

#         # Use GridFS to store and retrieve files
#         fs = gridfs.GridFS(db,collection="VideosDetection")

#         # Open the file with the specified name
#         file = fs.find_one({"filename": filename})

#         # Read the first chunk of the file
#         f=0
#         chunk = file.readchunk(f)

#         # Encode the chunk as base64
#         base64_encoded = base64.b64encode(chunk)

#         # Return the base64-encoded image data with the appropriate Content-Type header
#         return HttpResponse(base64_encoded, content_type='image/jpeg')


# @csrf_exempt
# def get_first_video_frame2(request):
#     db = mongo_connection()
#     fs = gridfs.GridFS(db,collection="VideosDetection")
#     # Get the file name from the request
#     # global filename
#     filename = request.GET.get("filename")
#     # filee=filename
#     # data=db.Rocket.VideosDetection.files
    
#     # Get the video file from the collection
#     file = fs.find_one({"filename": filename})
#     #print(file)

#     # Check if the file exists
#     # if file is None:
#     #     return HttpResponse("Error: File does not exist", status=404)
#     chunk = file.readchunk()
#     response = HttpResponse(content_type="image/jpeg")
#     response.write(chunk)
#     print("do")
#     return response
   
    
 







# import React, { useEffect, useState, useRef } from "react";
# import css from "./Main.module.css";
# import axios from "axios";
# import { SpinnerDiamond } from "spinners-react";
# import LoadingSpinnerButton from "./components/ButtunSpiner/LoadingSpinnerButton";

# const Streamvideo = () => {
#   const urlStream = "http://127.0.0.1:8000/video_feed/";
#   // const urlTest = "http://127.0.0.1:8000/data";
#   const urlDetaction = "http://127.0.0.1:8000/detection_percentage/";
#   // const change = useRef(null);
#   const [data, setData] = useState("");
#   const [children, setChildren] = useState([]);
#   const [isRunning, setIsRunning] = useState(true);
#   const [loading, setLoading] = useState(false);
#   const [click, setClick] = useState(false);
#   const [loadBeforeStrem, setShowBeforeStrem] = useState(true);
#   // const [checked, setChecked] = useState(false);
#   const snackbarRef = useRef(null);
#   //Datetime
#   const date = new Date();
#   const showTime =
#     date.getHours() + ":" + date.getMinutes() + ":" + date.getSeconds();

#   let flag = isRunning;
#   const start = -0.1;

#   const onLoadStart = (event) => {
#     event.preventDefault();

#     setLoading(true);
#     setClick(true);
#     /* Time taken by API to send data */
#     setTimeout(() => {
#       setLoading(false);
#       setShowBeforeStrem(false);
#     }, 1000);
#   };

#   const getDetection = async () => {
#     let flag = isRunning;
#     // const start = isToggled;
#     while (click && flag) {
#       console.log("before try isRunning,flag,start", isRunning, flag);
#       // console.log("in while buttonIsOn", buttonIsOn);
#       try {
#         const resp = await axios.get(urlDetaction);
#         console.log(resp);
#         let flag = resp.data.isRunning;
#         // console.log("in try buttonIsOn", buttonIsOn);
#         if (!isNaN(resp.data.det)) {
#           setData(resp.data.det);
#           // setData(start);
#           console.log("detection", resp.data.det);
#         }
#         if (flag === false) {
#           console.log("in flag start", flag);
#           break;
#         }
#       } catch (err) {
#         console.error(err);
#       }
#     }
#   };

#   useEffect(() => {
#     if (data > 0) {
#       setChildren((prev) => [
#         <div style={{ backgroundColor: getBackground(data) }}>
#           <h6>Detection:{data}</h6>
#           <h6> Cureent Time:{showTime}</h6>
#         </div>,
#         ...prev,
#       ]);
#     }
#   }, [data, showTime]);

#   useEffect(() => {
#     // console.log("buttonIsOn useeffect", buttonIsOn);
#     if (flag && click) {
#       getDetection();
#     }
#   }, [data, click]);

#   const getBackground = (data) => {
#     if (data > 0.01 && data <= 0.2) {
#       return "#fec9c9";
#     } else if (data > 0.2 && data <= 0.4) {
#       return "#ffa1a1";
#     } else if (data > 0.4 && data <= 0.6) {
#       return "#ff8080";
#     } else if (data > 0.6 && data <= 0.8) {
#       return "#ff5f5f";
#     } else if (data > 0.8 && data < 1) {
#       return "#ff0e0e";
#     }
#   };

#   return (
#     <div>
#       <div className={css.spiner}>
#         <LoadingSpinnerButton
#           title={"Load Data"}
#           loading={loading}
#           onClick={onLoadStart}
#         />
#       </div>
#       {click ? (
#         <img className={css.img} src={urlStream} alt="stream" />
#       ) : (
#         <div className={css.imgload}>
#           <SpinnerDiamond
#             style={{ marginLeft: 320, marginTop: 150 }}
#             size={150}
#             thickness={121}
#             speed={90}
#             color="rgba(110, 57, 172, 0.81)"
#             secondaryColor="rgba(57, 172, 154, 1)"
#           />
#         </div>
#       )}
#       {/* <ClipLoader
#           className={css.img}
#           loading={loadBeforeStrem}
#           size={150}
#           aria-label="Loading Spinner"
#           data-testid="loader"
#         /> */}
#       <div>
#         <div className={css.cat}>{children}</div>
#       </div>
#     </div>
#   );
# };

# export default Streamvideo;
















##nothing 15.1.23##





# @csrf_exempt
# async def video_feed(request):
#     # Check if this is a POST request
#     if request.method == 'POST':

#         # Get the URL of the video to stream from the request data
#         global content
#         content = request.GET.get('url', 'not')
#         print(content)
#     # Create a StreamingHttpResponse object with a generator function that will stream the video data
#     response = StreamingHttpResponse(stream(content), content_type='text/event-stream')
#     response['Cache-Control'] = 'no-cache'

#     # Await the generator function
#     await response
#     try:
#         for frame in response:
#             yield frame
#     except StopAsyncIteration:
#         pass
#     if response['X-Frame-Options'] is not None:
#         # Do something here
#         pass

# @csrf_exempt
# async def video_feed(request):
#     # Check if this is a POST request
#     if request.method == 'POST':
#         # Get the URL of the video to stream from the request data
#         global content
#         content = request.GET.get('url', 'not')
#         print(content)

#     # Create a StreamingHttpResponse object with a generator function that will stream the video data
#     response = StreamingHttpResponse(stream(content), content_type='text/event-stream')
#     response['Cache-Control'] = 'no-cache'

#     # Stream the frames
#     async for frame in response:
#         yield frame

    




# def upload_video_file_toMongo2(file_loc,file_name):
#     print("file loc at upload_video_file_toMongo",file_loc)
#     db = mongo_connection()
#     fs = gridfs.GridFS(db,collection="VideosDetection")
#     with open(file_loc,'rb') as file_data:
#         data = file_data.read()
#     # with open(json_file, "r") as f:
#     #     json_data = json.load(f)    
#     # ##put file into mongo DB
#     # metadata = {
#     #      "detectionData": json_data
#     # }
#     fs.put(data,filename=file_name)
#     print("Upload Complete!")   
        
# response = HttpResponse()
        # response.write(file.read())
        # response['Content-Type'] = 'video/mp4'
       
        # detection_data = file.metadata['detectionData']
        # detection_data_json = json.dumps(detection_data)
        # print("detectionData",detection_data)
        # response['detection_data'] = detection_data_json
        # print("type")
        # print(type(detection_data))
        # return response


        # add the metadata to the response
        # response['metadata'] = file.metadata
        # response.content = {'video': response.content, 'metadata': file.metadata}
        # return response
        # response['metadata'] = file.metadata
        # # convert the metadata field to a JSON-formatted string
        # metadata_json = json.dumps(detection_data)
        # # add the JSON-formatted metadata to the response body
        # response['metadata'] = metadata_json
        # return response       


# @csrf_exempt
# def load_video2(request):
#     if request.method == 'GET':
#         fileName = request.GET.get('filename','FailedGetFileName')
#         # connect_str = "mongodb+srv://ilay:asis2003@cluster0.2mtny9z.mongodb.net/?retryWrites=true&w=majority"
#         client = pymongo.MongoClient(connect_str)
#         db = client["Rocket"]
#         fs = gridfs.GridFS(db,collection="VideosDetection")
#         # Get all the files from MongoDB using the GridFS API
#         files = fs.find()
#         # file_name = fs.find_one({"filename":fileName})
#         # print("files found",file_name)
#          # Create an empty response
#         response = HttpResponse()
    
#          # Iterate over the files and add their content to the response
#         for file in files:
#             print(file)
#             response.write(file.read())
    
#             # Set the response's content type as text/html
#             response['Content-Type'] = 'video/mp4'
#         return response



# def get_video(request, video_id):
#     # Connect to the MongoDB database
#     db=mongo_connection

#     # Initialize the GridFS object
#     fs = gridfs.GridFS(db,collection="VideosDetection")

#     # Load the video file from the database using its ObjectId
#     video_file = fs.get(ObjectId(video_id))

#     # Create an HttpResponse object with the video file data as its content
#     response = HttpResponse(video_file.read(), content_type=video_file.content_type)

#     # Set the appropriate Content-Disposition header so the client knows to download the file
#     response['Content-Disposition'] = 'attachment; filename="{}"'.format(video_file.filename)


#     return response      
# def load_video2(request):
#     # Connect to the MongoDB database
#     #db = mongo_connection()
#     client = MongoClient("mongodb+srv://ilay:asis2003@cluster0.2mtny9z.mongodb.net/?retryWrites=true&w=majority")
#     db = client.mydatabase
#     # Initialize the GridFS object
#     fs = gridfs.GridFS(db)
#     print("fs respone",fs)
#     name="ResultOfVideo_MissileLaunch3.avi"
#     print("db.VideosDetection.files",db.VideosDetection.files.ResultOfVideo_MissileLaunch3.avi)
#     data=db.VideosDetection.files.find_one({"file_name":name})
#     print("data",data)
#     fs_id= data['_id']
#     out_data = fs.get(fs_id).read()
#     download ='C:/Users/ilaya/LaunchVideos'
#     with open(download,'wb') as output:
#         output.write(out_data)
#     # video_file = fs.get(gridfs.ObjectId("6394de78f95a550d414b454e"))
#     # print("video_file respone",video_file)
#     # file = fs.find_one({'filename': 'ResultOfVideo_MissileLaunch3.avi'})
#     # CRAWLED_FILE = os.path.join(SAVING_FOLDER, 'new_file.txt')
#     # with open(CRAWLED_FILE, 'wb') as f:
#     #     f.write(file.read())
#     # f.close()
#     # print(" file_doc ", file )
#     # file_id = file["_id"]
#     # # Load the video file from the database using its ObjectId
#     # video_file = fs.get(file_id)

#     # Create an HttpResponse object with the video file as its content
#     response = HttpResponse(output, content_type="video/mp4")

#     # # Set the appropriate Content-Disposition header so the client knows to download the file
#     response['Content-Disposition'] = 'attachment; filename="{}"'.format(output.filename)

#     return response










# confidence = conf.item()
 # print("confidenceJson",confidenceJson)         
           
# num_frames += 1
            # elapsed_time = time.perf_counter() - start_time
            
            # if elapsed_time > 1:
            #     # Calculate the frame rate
            #     fps = num_frames / elapsed_time
            #     fps = fps / 1
        
            #    # Set the frame rate of the output video
            #     out.set(cv2.CAP_PROP_FPS, int(fps))
            #     print(f"Frames Per Second : {fps}")
        
            
            # fps = 1/np.round(end_time - start_time, 3)
            # fps = fps / 1
            # print(f"Frames Per Second : {fps}")
           
            # previous_time_fps = current_time_fps    
 # frame= cv2.resize(frame,(1200,700))
            # current_time_fps = timer.perf_counter_ns()
            
            # framespersecond= int(cap.get(cv2.CAP_PROP_FPS))
            # print("framespersecond",framespersecond)
            # if previous_time_fps is not None:
            #     fps = 1 / ((current_time_fps - previous_time_fps) / 1000000000)
            #     # if fps < MIN_FPS:
            #     #    fps = MIN_FPS
            #     # elif fps > MAX_FPS:
            #     #     fps = MAX_FPS
            #     # print("fps" , fps )
                
            #     out.set(cv2.CAP_PROP_FPS, fps)
               
            #     # out.set(cv2.CAP_PROP_FPS, fps)
            #     #
            #     # timer.sleep(1.0 / fps)
            













##15.1.23 working##


#All FORM
from yolov5.utils.general import (check_img_size, non_max_suppression, scale_coords, 
                                  check_imshow, xyxy2xywh, increment_path)
from django.http import StreamingHttpResponse,HttpResponse,JsonResponse,HttpResponseNotFound
from yolov5.utils.torch_utils import select_device, time_sync
from django.views.decorators.http import require_http_methods
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_exempt
from yolov5.utils.plots import Annotator, colors
from deep_sort.utils.parser import get_config
from urllib.parse import urlparse,parse_qs
from deep_sort.deep_sort import DeepSort
from djongo.storage import GridFSStorage
from django.shortcuts import render
from multiprocessing import Process
from bson.objectid import ObjectId
from pymongo import MongoClient
from gridfs import GridFSBucket
from threading import Thread
from PIL import Image as im
from zipfile import ZipFile
from yolov5 import detect
from mydia import Videos
from io import BytesIO
from ast import While





#All IMPORT
import time
import yolov5,torch
import numpy as np
import logging
import pymongo
import pickle
import urllib
import base64
import gridfs
import json
import pafy
import cv2
import gridfs
# import constant
import sys
import os
import onnx
import sys

def index(request):
    return render(request,'index.html')
device = select_device('0') # 0 for gpu, '' for cpu

print(torch.cuda.is_available())
#load model
# model = YOLO(path='C:/Users/ilaya/trainningModels/TREX2Base/best.pt')
#model = torch.hub.load('ultralytics/yolov8', 'custom', path='C:/Users/ilaya/trainningModels/Rocket-Detect-27/best.pt',)
#model = torch.hub.load('ultralytics/yolov5', 'yolov5s','yolov5s.onnx')
#model = torch.hub.load('ultralytics/yolov5', 'custom',path='C:/Users/ilaya/trainningModels/TREX2FitWithin/best.pt',device=device)
model = torch.hub.load('ultralytics/yolov5', 'custom',path='C:/Users/ilaya/trainningModels/pro/best.pt',device=device)
#model = torch.hub.load('ultralytics/yolov','custom',path='C:/Users/ilaya/trainningModels/TREX2FitWithin/best.pt',device=device)

# model = torch.hub.load('ultralytics/yolov5', 'custom',path='C:/Users/ilaya/trainningModels/TREX2Base/best.pt',device=device)
#model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:/Users/ilaya/trainningModels/Rocket-Detect-32/300epmodel5n/best.pt',device=device)


# initialize deepsort
# cfg = get_config()
# cfg.merge_from_file("deep_sort/configs/deep_sort.yaml")
# deepsort = DeepSort('osnet_x0_25',
#                     device,
#                     max_dist=cfg.DEEPSORT.MAX_DIST,
#                     max_iou_distance=cfg.DEEPSORT.MAX_IOU_DISTANCE,
#                     max_age=cfg.DEEPSORT.MAX_AGE, n_init=cfg.DEEPSORT.N_INIT, nn_budget=cfg.DEEPSORT.NN_BUDGET,
#                     )

# Get names and colors

names = model.module.names if hasattr(model, 'module') else model.names

print("name",names)


startvideo = False
confidence = None
check = True
end=True
det=0
# global num_frames,elapsed_time,start_time
# num_frames = 0
# elapsed_time = 0
# start_time = time.perf_counter()


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


def stream(source):
    end = False
    detection_data = []
    if startvideo : 
        global file_loc,file_name,fs,check,confidence,time_to_detect,det,previous_time_fps
        time_to_detect = 0
        path_to_frame = None
        frame_counter = 0
        source=content
        locationvideo = content.split("/")
        video_name=locationvideo[-1]
        url = source + str('.mp4')
        saveName = str('ResultOfVideo_') +str(video_name) + str('.mp4')
        saveNameJson =  str('ResultOfVideo_') +str(video_name)
        file_name=saveName
        device = select_device('0')
        path_to_save_video = "C:/Users/ilaya/LaunchVideos/VideoAfter/"
        laoction_name = path_to_save_video + saveName
        file_loc=laoction_name
        fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        out = cv2.VideoWriter(laoction_name,fourcc,30,(416, 416))
        cap = cv2.VideoCapture(url)
        cap.set(cv2.CAP_PROP_FPS, 120) 
        cap.set(cv2.CAP_PROP_CONVERT_RGB, 1)

        cap.set(cv2.CAP_PROP_FPS, 60) 

        print("Source",source)
        print("video_name",video_name)
        print("url:",url)
        print("laoction_name",laoction_name)
        print("url",url)
        path_uplode_video_withDetrction = (path_to_save_video) + (saveName)
        imageWidth = int(cap.get(3))
        imageHeight = int(cap.get(4))
        fps = cap.get(cv2.CAP_PROP_FPS)
        model.conf=0.355
        flagTime = True
        while (cap.isOpened()):
            if(flagTime):
                startS = time.time()
                flagTime = False

            frame_counter += 1
            # if(frame_counter) % 10!= 0:
            #     continue
            check = True
            ret, frame = cap.read()
            start_time = time.perf_counter()
            if not ret:
                print("Error: failed to capture image")
                check = False
                print(str('Completed video ') + str(saveName))
                endE = time.time()
                break
            frame = cv2.resize(frame, (320, 320))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = model(frame,augment=False,size=320)
            end_time = time.perf_counter()
            fps = 1 / np.round(end_time - start_time, 3)
            print("FPS :" , fps)
            det = results.pred[0]
            results.render()
            out.write(frame)   
            confidence=0.5;
            for *xyxy, conf, cls in det:
                floatNum=torch.IntTensor.item(conf)
                num=f"{floatNum:.2f}"
                detection_conf = float(num)
                confidence = detection_conf
                path_to_frame =  "C:/Users/ilaya/LaunchVideos/Frame/BestFrameFor" +  str(saveName) + ".jpg"
                # if confidence > 0.6:
                #     cv2.imwrite(path_to_frame,frame)
                # end = time.time()
                time_to_detect = 0
                x1 = int(xyxy[0].item())
                y1 = int(xyxy[1].item())
                x2 = int(xyxy[2].item())
                y2 = int(xyxy[3].item())
                width = x2 - x1
                height = y2 - y1
                surface_area = width * height
                detection_data.append({
                    "coordinates": [x1,y1,x2,y2],
                    "confidence": confidence,
                    "surface_area": surface_area,
                    "time": time_to_detect
                })
            # confidence=0.5
            annotator = Annotator(frame,line_width=2, pil=not ascii)
            im0 = annotator.result()
            image_bytes = cv2.imencode('.jpg', im0)[1].tobytes()
            
            yield (b'--frame\r\n'
                  b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n')

        cap.release()
        out.release()
        
        elapsed_time_ms = ( endE - startS ) 
        print("time",elapsed_time_ms)
        # print("frame_counter",frame_counter)
        cv2.destroyAllWindows()
        # json_file_name = "detection_data_" + str(saveNameJson)+str(".json")
        # with open(json_file_name, "w") as f:
        #     json.dump(detection_data, f)
        end = True
        # print("json_file_name",json_file_name)
        # print("file_loc at end",file_loc,"filename",file_name)
    if end:
        print("done")
        # upload_video_file_toMongo(file_loc=file_loc,file_name=file_name,json_file=json_file_name,path_to_frame=path_to_frame)




def upload_video_file_toMongo(file_loc,file_name,json_file,path_to_frame):
    pathForUploadPhoto = path_to_frame
    print("file loc at upload_video_file_toMongo",file_loc)
    db = mongo_connection()
    fs = gridfs.GridFS(db,collection="VideosDetection")

    with open(file_loc,'rb') as file_data:
        data = file_data.read()
    with open(json_file, "r") as f:
        json_data = json.load(f)    
    with open(pathForUploadPhoto, "rb") as f:
        image_data = f.read()

    metadata = {
        "detectionData": json_data,
        "image": image_data
    }

    #Check if a file with the same name already exists in the collection
    existing_file = fs.find_one({"filename": file_name})

    # Update the file if it already exists
    if existing_file is not None:
        # Delete the existing file
        fs.delete(existing_file._id)
        #Re-upload the file with the new data and metadata
        fs.put(data, filename=file_name, metadata=metadata)
        print("File updated successfully")
    else:
        # Add the new file to the collection
        fs.put(data, filename=file_name, metadata=metadata)
        print("File added successfully")


def get_first_video_frame(path_to_frame,file_name,json_file):
    fileNameToUpload=file_name
    pathForUploadPhoto = path_to_frame
    connect_str = "mongodb+srv://ilay:asis2003@cluster0.2mtny9z.mongodb.net/?retryWrites=true&w=majority"
    client = pymongo.MongoClient(connect_str)
    db = client["Rocket"]
    fs = gridfs.GridFS(db,collection="VideosDetection")
    with open(pathForUploadPhoto, "rb") as f:
        image_data = f.read()
    with open(json_file, "r") as f:
        json_data = json.load(f)    
    file_id = fs.find_one({"filename": fileNameToUpload})._id
    print("file id",file_id)
    #put file into mongo DB
    metadata = {
        "detectionData": json_data,
        "image": image_data
    }
    #metadata = db.fs.files.find_one({"_id": file_id}, {"metadata": 1})
    # db.VideosDetection.files.update_one({"_id": file_id}, {"$set": {"metadata": metadata}})
    update_metadata(file_id,metadata)
    metadata = db.VideosDetection.files.find_one({"_id": file_id}, {"metadata": 1})
    image_data = metadata["metadata"]["image"]
    with open("image.jpg", "wb") as f:
        f.write(image_data)
    # Display the image using an image library such as Pillow
    imageResult = im.open(BytesIO(image_data))
    imageResult.show()

def update_metadata(file_id, metadata):
    # Connect to the MongoDB database
    connect_str = "mongodb+srv://ilay:asis2003@cluster0.2mtny9z.mongodb.net/?retryWrites=true&w=majority"
    client = pymongo.MongoClient(connect_str)
    db = client["Rocket"]
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
    # Connect to the MongoDB database
    connect_str = "mongodb+srv://ilay:asis2003@cluster0.2mtny9z.mongodb.net/?retryWrites=true&w=majority"
    client = pymongo.MongoClient(connect_str)
    db = client["Rocket"]
    fs = gridfs.GridFS(db,collection="VideosDetection")

    # Find all the files in the database
    files = fs.find()

    data = []
    # Iterate through the files and extract the metadata and filename
    for file in files:
        metadata = file.metadata
        filename = file.filename
    
        # Convert the binary data in the metadata to a base64-encoded string
        if 'image' in metadata:
            image_data = metadata['image']
            metadata['image'] = base64.b64encode(image_data).decode('utf-8')

        data.append({'filename': filename, 'metadata': metadata})

    # Return the data as a JSON response
    return HttpResponse(json.dumps(data), content_type='application/json')

def detection():
    while True:
        if(not check):
            data={"isRunning":False,"passtime":time_to_detect}
            dataJson=json.dumps(data)        
            return dataJson
        if(confidence is not None  and len(det) > 0):
            data={"det":confidence,"isRunning":True,"passtime":time_to_detect}
            dataJson=json.dumps(data)
            return dataJson
        data={"isRunning":True}
        dataJson=json.dumps(data) 
        return dataJson

@csrf_exempt
def video_feed(request):
    if request.method == 'POST':
        global content
        global start
        content = request.GET.get('url','not')
        print(content)  
    video_thread = Thread(target=stream, args=(content,))
    detection_thread = Thread(target=detection)
    video_thread.start()
    detection_thread.start()      
    return StreamingHttpResponse(stream(content), content_type='multipart/x-mixed-replace; boundary=frame')   


def detection_percentage(request):
    video_thread = Thread(target=stream, args=(content,))
    detection_thread = Thread(target=detection)
    video_thread.start()
    detection_thread.start()
    global startvideo
    startvideo=True
    return HttpResponse(detection())



@csrf_exempt
def load_video(request):
    if request.method == 'GET':
        #get the fileName
        fileName = request.GET.get('filename','FailedGetFileName')
        #connect to db
        connect_str = "mongodb+srv://ilay:asis2003@cluster0.2mtny9z.mongodb.net/?retryWrites=true&w=majority"
        client = pymongo.MongoClient(connect_str)
        db = client["Rocket"]
        fs = gridfs.GridFS(db,collection="VideosDetection")
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

        detection_data = fs.find_one({"filename": fileName}).metadata['detectionData']
       

        # convert the detection data to a JSON-formatted string
        detection_data_json = json.dumps(detection_data)
        print("detection_data",detection_data_json)

        # create a dictionary with the video and detection data
        response_data = {'video': file_contents_base64, 'detectionData': detection_data_json}


        # return the response as JSON
        return HttpResponse(json.dumps(response_data), content_type='application/json')














                   # confidence = conf.item()
                # print("confidenceJson",confidenceJson)         
           
            # num_frames += 1
            # elapsed_time = time.perf_counter() - start_time
            
            # if elapsed_time > 1:
            #     # Calculate the frame rate
            #     fps = num_frames / elapsed_time
            #     fps = fps / 1
        
            #    # Set the frame rate of the output video
            #     out.set(cv2.CAP_PROP_FPS, int(fps))
            #     print(f"Frames Per Second : {fps}")
        
            
            # fps = 1/np.round(end_time - start_time, 3)
            # fps = fps / 1
            # print(f"Frames Per Second : {fps}")
           
            # previous_time_fps = current_time_fps    
 # frame= cv2.resize(frame,(1200,700))
            # current_time_fps = timer.perf_counter_ns()
            
            # framespersecond= int(cap.get(cv2.CAP_PROP_FPS))
            # print("framespersecond",framespersecond)
            # if previous_time_fps is not None:
            #     fps = 1 / ((current_time_fps - previous_time_fps) / 1000000000)
            #     # if fps < MIN_FPS:
            #     #    fps = MIN_FPS
            #     # elif fps > MAX_FPS:
            #     #     fps = MAX_FPS
            #     # print("fps" , fps )
                
            #     out.set(cv2.CAP_PROP_FPS, fps)
               
            #     # out.set(cv2.CAP_PROP_FPS, fps)
            #     #
            #     # timer.sleep(1.0 / fps)
            


# @csrf_exempt
# async def video_feed(request):
#     # Check if this is a POST request
#     if request.method == 'POST':

#         # Get the URL of the video to stream from the request data
#         global content
#         content = request.GET.get('url', 'not')
#         print(content)
#     # Create a StreamingHttpResponse object with a generator function that will stream the video data
#     response = StreamingHttpResponse(stream(content), content_type='text/event-stream')
#     response['Cache-Control'] = 'no-cache'

#     # Await the generator function
#     await response
#     try:
#         for frame in response:
#             yield frame
#     except StopAsyncIteration:
#         pass
#     if response['X-Frame-Options'] is not None:
#         # Do something here
#         pass

# @csrf_exempt
# async def video_feed(request):
#     # Check if this is a POST request
#     if request.method == 'POST':
#         # Get the URL of the video to stream from the request data
#         global content
#         content = request.GET.get('url', 'not')
#         print(content)

#     # Create a StreamingHttpResponse object with a generator function that will stream the video data
#     response = StreamingHttpResponse(stream(content), content_type='text/event-stream')
#     response['Cache-Control'] = 'no-cache'

#     # Stream the frames
#     async for frame in response:
#         yield frame

    




# def upload_video_file_toMongo2(file_loc,file_name):
#     print("file loc at upload_video_file_toMongo",file_loc)
#     db = mongo_connection()
#     fs = gridfs.GridFS(db,collection="VideosDetection")
#     with open(file_loc,'rb') as file_data:
#         data = file_data.read()
#     # with open(json_file, "r") as f:
#     #     json_data = json.load(f)    
#     # ##put file into mongo DB
#     # metadata = {
#     #      "detectionData": json_data
#     # }
#     fs.put(data,filename=file_name)
#     print("Upload Complete!")   
        
# response = HttpResponse()
        # response.write(file.read())
        # response['Content-Type'] = 'video/mp4'
       
        # detection_data = file.metadata['detectionData']
        # detection_data_json = json.dumps(detection_data)
        # print("detectionData",detection_data)
        # response['detection_data'] = detection_data_json
        # print("type")
        # print(type(detection_data))
        # return response


        # add the metadata to the response
        # response['metadata'] = file.metadata
        # response.content = {'video': response.content, 'metadata': file.metadata}
        # return response
        # response['metadata'] = file.metadata
        # # convert the metadata field to a JSON-formatted string
        # metadata_json = json.dumps(detection_data)
        # # add the JSON-formatted metadata to the response body
        # response['metadata'] = metadata_json
        # return response       


# @csrf_exempt
# def load_video2(request):
#     if request.method == 'GET':
#         fileName = request.GET.get('filename','FailedGetFileName')
#         # connect_str = "mongodb+srv://ilay:asis2003@cluster0.2mtny9z.mongodb.net/?retryWrites=true&w=majority"
#         client = pymongo.MongoClient(connect_str)
#         db = client["Rocket"]
#         fs = gridfs.GridFS(db,collection="VideosDetection")
#         # Get all the files from MongoDB using the GridFS API
#         files = fs.find()
#         # file_name = fs.find_one({"filename":fileName})
#         # print("files found",file_name)
#          # Create an empty response
#         response = HttpResponse()
    
#          # Iterate over the files and add their content to the response
#         for file in files:
#             print(file)
#             response.write(file.read())
    
#             # Set the response's content type as text/html
#             response['Content-Type'] = 'video/mp4'
#         return response



# def get_video(request, video_id):
#     # Connect to the MongoDB database
#     db=mongo_connection

#     # Initialize the GridFS object
#     fs = gridfs.GridFS(db,collection="VideosDetection")

#     # Load the video file from the database using its ObjectId
#     video_file = fs.get(ObjectId(video_id))

#     # Create an HttpResponse object with the video file data as its content
#     response = HttpResponse(video_file.read(), content_type=video_file.content_type)

#     # Set the appropriate Content-Disposition header so the client knows to download the file
#     response['Content-Disposition'] = 'attachment; filename="{}"'.format(video_file.filename)


#     return response      
# def load_video2(request):
#     # Connect to the MongoDB database
#     #db = mongo_connection()
#     client = MongoClient("mongodb+srv://ilay:asis2003@cluster0.2mtny9z.mongodb.net/?retryWrites=true&w=majority")
#     db = client.mydatabase
#     # Initialize the GridFS object
#     fs = gridfs.GridFS(db)
#     print("fs respone",fs)
#     name="ResultOfVideo_MissileLaunch3.avi"
#     print("db.VideosDetection.files",db.VideosDetection.files.ResultOfVideo_MissileLaunch3.avi)
#     data=db.VideosDetection.files.find_one({"file_name":name})
#     print("data",data)
#     fs_id= data['_id']
#     out_data = fs.get(fs_id).read()
#     download ='C:/Users/ilaya/LaunchVideos'
#     with open(download,'wb') as output:
#         output.write(out_data)
#     # video_file = fs.get(gridfs.ObjectId("6394de78f95a550d414b454e"))
#     # print("video_file respone",video_file)
#     # file = fs.find_one({'filename': 'ResultOfVideo_MissileLaunch3.avi'})
#     # CRAWLED_FILE = os.path.join(SAVING_FOLDER, 'new_file.txt')
#     # with open(CRAWLED_FILE, 'wb') as f:
#     #     f.write(file.read())
#     # f.close()
#     # print(" file_doc ", file )
#     # file_id = file["_id"]
#     # # Load the video file from the database using its ObjectId
#     # video_file = fs.get(file_id)

#     # Create an HttpResponse object with the video file as its content
#     response = HttpResponse(output, content_type="video/mp4")

#     # # Set the appropriate Content-Disposition header so the client knows to download the file
#     response['Content-Disposition'] = 'attachment; filename="{}"'.format(output.filename)

#     return response















##5.2##
from asgiref.sync import async_to_sync
import json
from channels.generic.websocket import AsyncWebsocketConsumer
import cv2
import json
from django.http import JsonResponse
from asgiref.sync import async_to_sync
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer
import asyncio
import base64
import torch
from yolov5.utils.plots import Annotator
from yolov5.utils.torch_utils import select_device

# from ultralytics import YOLO
#from ultralytics.yolo.v8.detect.predict import Detection
device = select_device('0')
#model = torch.hub.load('ultralytics/yolov5', 'custom',path='C:/Users/ilaya/trainningModels/pro/best.pt',device=device)
# model = torch.hub.load('WongKinYiu/yolov7', 'custom', 'C:/Users/ilaya/trainningModels/proV7/whilerunning/best.pt',
#                         trust_repo=True)

model = torch.hub.load('ultralytics/yolov5', 'custom',path='C:/Users/ilaya/trainningModels/MoreEp/best.pt',device=device)
import time
model=model.to(device)
# model.classes= "Rocket Body"
model.iou = 0.2
model.conf = 0.4
class StreamConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        await self.accept()
        url = "C:/Users/ilaya/LaunchVideos/VideoBefore/MissileLaunch1.mp4"
        self.camera = cv2.VideoCapture(url)
        fps = self.camera.get(cv2.CAP_PROP_FPS)
        print("fps",fps)
        imageWidth = int(self.camera.get(3))
        imageHeight = int(self.camera.get(4))
        frame_count = int(self.camera.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = frame_count / fps
        
        # 1000th/fps  will equql the time 
        # if  we keep frame count right ,fps same it will get same time.
        self.camera.set(cv2.CAP_PROP_CONVERT_RGB, 1)
        async def send_frames():
            current_frame = 1
            # self.camera.set(cv2.CAP_PROP_FPS, 90）
            start_time = time.time()
            # keep 
            fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
            out = cv2.VideoWriter("C:/Users/ilaya/LaunchVideos/VideoAfter/MissileLaunch10.mp4",fourcc,fps,(imageWidth, imageHeight))
            startAll = time.time()
            while True:
                ret, frame = self.camera.read()
                # his 1st frame , or 2nd
                # fps is same, so in anyvieo with smae order or frames, have same time of nth farme.
                if not ret:
                    endAll = time.time()
                    print("Length of time between first frame and last frame: ", duration)
                    end_All_video = ( endAll - startAll ) 
                    print("actually",end_All_video)
                    break
                # startTime = time.time()
                if ret:
                    
                    frame = cv2.resize(frame, (640, 640))
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    results = model(frame,augment=False,size=640)
                    results.render()
                    # GPU such as NVIDA P1
                    out.write(frame)
                    _, buffer = cv2.imencode('.jpg', frame)
                    encoded_frame = base64.b64encode(buffer).decode()
                    labels, cord = results.xyxyn[0][:, -1].cpu().numpy(), results.xyxyn[0][:, :-1].cpu().numpy()
                    n = len(labels)
                    confidence = 0
                    for i in range(n):
                        row = cord[i]
                        confidenceFloat=row[4]
                        confidence=f"{confidenceFloat:.2f}"
                        print("confidence : ",confidence)                       
                    
                        # elapsed_time_fps= time.time() - start_time_fps
                        # fps = frame_count / elapsed_time_fps
                        # print("FPS:",fps)

                    # key point -  match curretntime-confidence.
                    current_time = current_frame / fps
                    print("current_time",current_time)
                    current_frame += 1
                    print("current_frame",current_frame,"")
                    await self.send(json.dumps({'frame': encoded_frame,"time":current_time,"confidence":str(confidence)}))
                    elapsed_time = time.time() - start_time
                    print("Elapsed time: ", current_time)
                await asyncio.sleep(0.000001)
        await send_frames()

    async def disconnect(self, close_code):    
        self.camera.release()
