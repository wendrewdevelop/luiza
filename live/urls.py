from django.urls import path
from live.api.viewsets import StreamAPI


urlpatterns = [
    path(
        'api/stream/', 
        StreamAPI.as_view(), 
        name='stream-api'
    ),
]
