from django.contrib import admin
from django.urls import path
from webcam import views
# from .views import DetectionData
from . import views
urlpatterns = [
   # path('video_feed/', views.video_feed, name='video_feed'),
   path('load_video/', views.load_video, name='load_video'),
   # path('get_first_video_frame/', views.get_first_video_frame, name='get_first_video_frame'),
   path('get_files/', views.get_files, name='get_files'),
]