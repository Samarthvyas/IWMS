import os
from rest_framework import serializers
from .models import WasteReport

class WasteReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = WasteReport
        fields = '__all__'
        read_only_fields = ['user', 'waste_type', 'ai_confidence']

    def validate_image(self, value):

        allowed_extensions = ['.jpg', '.jpeg', '.png']

        extension = os.path.splitext(value.name)[1].lower()

        if extension not in allowed_extensions:
            raise serializers.ValidationError(
                "Only JPG, JPEG and PNG images are allowed."
            )

        return value    