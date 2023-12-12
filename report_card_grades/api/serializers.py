from rest_framework import serializers
from report_card_grades.models import ReportCard


class ReportCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportCard
        fields = '__all__'