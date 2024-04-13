from rest_framework import serializers
from .models import Adverts
from likes.models import Likes
from adoptions.models import Adoption

class AdvertSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    like_id = serializers.SerializerMethodField()
    adoption_id = serializers.SerializerMethodField()

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

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Likes.objects.filter(
                owner=user, advert=obj
            ).first()
            return like.id if like else None
        return None

    def get_adoption_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            adoption = Adoption.objects.filter(
                owner=user, advert=obj
            ).first()
            return adoption.id if adoption else None
        return None

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
            'other_animals',
            'content',
            'image',
            'is_owner',
            'like_id',
            'adoption_id',
        ]
