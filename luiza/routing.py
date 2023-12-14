from django.urls import re_path
from live.channel import VideoConsumer


websocket_urlpatterns = [
    re_path(r'ws/stream/$', VideoConsumer.as_asgi()),
]
