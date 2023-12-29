from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from administrative.models import Administrative
from administrative.api.serializers import AdministrativeSerializer
from user.permissions import UserPermission


class AdministrativeViewset(ModelViewSet):
    serializer_class = AdministrativeSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [UserPermission]

    def get_queryset(self):
        # if self.request.user
        return Administrative.objects.all()
    
    def list(self, request, *args, **kwargs):
        return super(AdministrativeViewset, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(AdministrativeViewset, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(AdministrativeViewset, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(AdministrativeViewset, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(AdministrativeViewset, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(AdministrativeViewset, self).partial_update(request, *args, **kwargs)