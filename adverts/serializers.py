from rest_framework import serializers
from .models import Adverts

class AdvertSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2: # 2MB in bytes
            raise serializers.ValidationError(
                "Image size larger than 2MB!"
            )
        if value.image.width > 500:
            raise serializers.ValidationError(
                "Image width is larger than 500px"
            )
        if value.image.height > 600:
            raise serializers.ValidationError(
                "Image height is larger than 600px"
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Adverts
        fields = [
            'id', 
            'owner',
            'created_at',
            'updated_at',
            'title',
            'name',
            'age',
            'breed',
            'sex',
            'children',
            'other_pets',
            'content',
            'image',
            'is_owner'
        ]
