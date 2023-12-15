from rest_framework import serializers
from administrative.models import Administrative


class AdministrativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrative
        fields = '__all__'