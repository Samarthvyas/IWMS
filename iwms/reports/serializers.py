from rest_framework import serializers
from .models import WasteReport

class WasteReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = WasteReport
        fields = '__all__'