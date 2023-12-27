from django.db import models
from rest_framework import serializers
from scheduler.models import Scheduler


class SchedulerSerializer(serializers.ModelSerializer):
    day = serializers.SerializerMethodField()

    def get_day(self, obj):
        return obj.created_at.day if obj.created_at else None
    class Meta:
        model = Scheduler
        fields = '__all__'