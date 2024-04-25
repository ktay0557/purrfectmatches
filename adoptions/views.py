from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Adoption
from .serializers import AdoptionSerializer
from purrfectmatches.permissions import IsOwnerOrReadOnly


class AdoptionList(generics.ListCreateAPIView):
    serializer_class = AdoptionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Adoption.objects.all()
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__profile',
    ]
    search_fields = [
        'name',
        'email',
        'mobile',
        'advert_id',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class AdoptionDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AdoptionSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Adoption.objects.all()

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]
        return super().get_permissions()
