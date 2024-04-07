from rest_framework import serializers
from .models import Adverts

class AdvertSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

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
