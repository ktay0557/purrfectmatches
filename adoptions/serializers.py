from rest_framework import serializers
from .models import Adoption

class AdoptionSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)

    class Meta:
        model = Adoption
        fields = [
            'id',
            'owner',
            'advert',
            'created_at',
            'name',
            'email',
            'mobile',
            'content'
        ]
