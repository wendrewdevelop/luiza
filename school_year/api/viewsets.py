from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import filters
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from school_year.models import SchoolYear
from school_year.api.serializers import SchoolYearSerializer
from user.permissions import UserPermission


class SchoolYearViewset(ModelViewSet):
    serializer_class = SchoolYearSerializer
    # permission_classes = [UserPermission]

    def get_queryset(self):
        return SchoolYear.objects.all()
    
    def list(self, request, *args, **kwargs):
        return super(SchoolYearViewset, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(SchoolYearViewset, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(SchoolYearViewset, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(SchoolYearViewset, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(SchoolYearViewset, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(SchoolYearViewset, self).partial_update(request, *args, **kwargs)