from rest_framework.viewsets import ModelViewSet
from classes.models import Video
from classes.api.serializers import VideoSerializer
from user.permissions import UserPermission


class VideoViewset(ModelViewSet):
    serializer_class = VideoSerializer
    permission_classes = [UserPermission]

    def get_queryset(self):
        return Video.objects.all()
    
    def list(self, request, *args, **kwargs):
        return super(VideoViewset, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(VideoViewset, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(VideoViewset, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(VideoViewset, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(VideoViewset, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(VideoViewset, self).partial_update(request, *args, **kwargs)