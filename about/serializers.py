from rest_framework import serializers
from .models import About

class AboutSerializer(serializers.ModelSerializer):
    """
    Serializer for the About model.
    Has image validation so an image used will not over fill the page. 
    """
    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2: # 2MB in bytes
            raise serializers.ValidationError(
                "Image size larger than 2MB!"
            )
        if value.image.width > 700:
            raise serializers.ValidationError(
                "Image width is larger than 700px"
            )
        if value.image.height > 800:
            raise serializers.ValidationError(
                "Image height is larger than 800px"
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
