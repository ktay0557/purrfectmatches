from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer
from purrfectmatches.permissions import IsOwnerOrReadOnly

class ProfileList(generics.ListAPIView):
    """
    List all the profiles
    Don't need create view (post method), django signals handles profile creation
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve and edit profiles using profile IDs
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
