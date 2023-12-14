from rest_framework import serializers
from rules.models import Rules


class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rules
        fields = '__all__'