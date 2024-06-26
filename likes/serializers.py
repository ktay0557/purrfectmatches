from django.db import IntegrityError
from rest_framework import serializers
from .models import Likes


class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model
    Create method handles the unique constraint on 'owner' and 'advert' 
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Likes
        fields = [
            'id', 
            'owner',
            'advert',
            'created_at'
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'potential duplicate'
            })
