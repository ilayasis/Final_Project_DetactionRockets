"""
ASGI config for stream project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
# from webcam.consumers import DetectionConsumer
import webcam.routing
from django.urls import path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stream.settings')


from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter

# application = ProtocolTypeRouter({
#     'http': get_asgi_application()
# })

application = ProtocolTypeRouter({
  'http': get_asgi_application(),
  'websocket':AuthMiddlewareStack(URLRouter(
    webcam.routing.websocket_urlpatterns
  ))
})



# application = ProtocolTypeRouter({
#   'websocket':AllowedHostsOriginValidator(
#     URLRouter([
#             path('',DetectionConsumer)
#     ])
#   )
# })


# application = get_asgi_application()

