from django.urls import re_path
# from .consumers import DetectionConsumer

from channels.security.websocket import AllowedHostsOriginValidator
from channels.routing import ProtocolTypeRouter,URLRouter
from . import consumers
from django.urls import path,re_path

websocket_urlpatterns = [
     re_path(r'ws/stream/', consumers.StreamConsumer.as_asgi()),
]
