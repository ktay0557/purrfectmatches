from rest_framework import serializers
from .models import Adoption
from adverts.models import Adverts

class AdoptionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    advert_id = serializers.PrimaryKeyRelatedField(queryset=Adverts.objects.all(), write_only=True)

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        advert_id = validated_data.pop('advert_id')
        validated_data['advert'] = Adverts.objects.get(id=advert_id)
        return super().create(validated_data)
        
    class Meta:
        model = Adoption
        fields = [
            'id',
            'owner',
            'advert_id',
            'created_at',
            'name',
            'email',
            'mobile',
            'content',
        ]