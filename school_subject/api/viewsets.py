from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from school_subject.models import Subject
from school_subject.api.serializers import SubjectSerializer
from user.permissions import UserPermission


class SubjectViewset(ModelViewSet):
    serializer_class = SubjectSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [UserPermission]

    def get_queryset(self):
        return Subject.objects.all()
    
    def list(self, request, *args, **kwargs):
        return super(SubjectViewset, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(SubjectViewset, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(SubjectViewset, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(SubjectViewset, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(SubjectViewset, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(SubjectViewset, self).partial_update(request, *args, **kwargs)