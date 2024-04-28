from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')
    is_staff_user = serializers.SerializerMethodField()

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image', 'is_staff_user'
        )

    """
    credit: https://github.com/MichelleBritton/fabfurryfriends/
    blob/3611858db311b8c365dc63d9b992651ca6431eea/fabfurryfriends/serializers.py#L20
    """

    def get_is_staff_user(self, obj):
        return obj.is_staff  # this will return true for self.is_staff user