from django.db.models import Q
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from inventory.models import Inventory
from inventory.api.serializers import InventorySerializer
from user.permissions import UserPermission


class InventoryViewset(ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [UserPermission]

    def get_queryset(self):
        queryset = Inventory.objects.all()

        return queryset
    
    def list(self, request, *args, **kwargs):
        return super(InventoryViewset, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(InventoryViewset, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(InventoryViewset, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(InventoryViewset, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(InventoryViewset, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(InventoryViewset, self).partial_update(request, *args, **kwargs)