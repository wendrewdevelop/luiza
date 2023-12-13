from django.db.models import Q
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from scheduler.models import Scheduler
from scheduler.api.serializers import SchedulerSerializer
from user.permissions import UserPermission
from user.models import User


class SchedulerViewset(ModelViewSet):
    queryset = Scheduler.objects.all()
    serializer_class = SchedulerSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [UserPermission]

    def get_queryset(self):
        queryset = Scheduler.objects.all()

        if self.request.user.user_type == 'student':
            queryset = queryset.filter(
                Q(visibility='public') | Q(visibility='private')
            )
        elif self.request.user.user_type == 'admin' or self.request.user.user_type == 'teacher':
            queryset = queryset.filter(
                visibility='public'
            )

        return queryset
    
    def create(self, request, *args, **kwargs):
        data = request.data
        visibility = None

        match self.request.user.user_type:
            case 'student':
                visibility = 'private'
            case 'teacher' | 'admin':
                visibility = 'public'

        instance = Scheduler.objects.create(
            created_by=self.request.user,
            day=data['day'],
            month=data['month'],
            year=data['year'],
            title=data['title'],
            description=data['description'],
            visibility=visibility
        )
            
        serializer = SchedulerSerializer(instance)
        return Response(serializer.data)