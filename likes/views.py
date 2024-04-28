from rest_framework import generics, permissions
from purrfectmatches.permissions import IsOwnerOrReadOnly
from .models import Likes
from .serializers import LikeSerializer


class LikeList(generics.ListCreateAPIView):
    """
    List likes or like something if logged in. 
    """
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Likes.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a like or delete it by id if the user is the owner. 
    """
    serializer_class = LikeSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Likes.objects.all()
