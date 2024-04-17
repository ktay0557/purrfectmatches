from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from purrfectmatches.permissions import IsOwnerOrReadOnly
from .models import Likes
from .serializers import LikeSerializer


class LikeList(generics.ListCreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Likes.objects.all()
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = ['advert']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    serializer_class = LikeSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Likes.objects.all()
