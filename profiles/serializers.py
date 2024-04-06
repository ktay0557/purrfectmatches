from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Profile
        fields = [
            'id', 
            'owner',
            'created_at',
            'updated_at',
            'name',
            'age',
            'email',
            'mobile',
            'location',
            'previously_owned',
            'currently_own',
            'relationship_status',
            'children',
            'housing',
            'hobbies',
            'preferred_breed',
            'preferred_age',
            'preferred_sex',
            'image',
            'is_staff'
        ]
