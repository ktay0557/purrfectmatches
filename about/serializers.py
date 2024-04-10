from rest_framework import serializers
from .models import About

class AboutSerializer(serializers.ModelSerializer):
    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2: # 2MB in bytes
            raise serializers.ValidationError(
                "Image size larger than 2MB!"
            )
        if value.image.width > 700:
            raise serializers.ValidationError(
                "Image width is larger than 500px"
            )
        if value.image.height > 800:
            raise serializers.ValidationError(
                "Image height is larger than 600px"
            )
        return value

    class Meta:
        model = About
        fields = [
            'id', 
            'created_at',
            'updated_at',
            'title',
            'content',
            'image',
        ]
