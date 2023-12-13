from rest_framework import serializers
from school_year.models import SchoolYear


class SchoolYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolYear
        fields = '__all__'