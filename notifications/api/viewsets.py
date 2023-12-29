from django.db.models import Q
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from notifications.models import Notification
from notifications.api.serializers import NotificationSerializer
from user.permissions import UserPermission
from user.models import User


class NotificationViewset(ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [UserPermission]

    def get_queryset(self):
        queryset = Notification.objects.all()

        return queryset
    
    def list(self, request, *args, **kwargs):
        return super(NotificationViewset, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(NotificationViewset, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(NotificationViewset, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(NotificationViewset, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(NotificationViewset, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(NotificationViewset, self).partial_update(request, *args, **kwargs)