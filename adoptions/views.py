from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Adoption
from .serializers import AdoptionSerializer
from purrfectmatches.permissions import IsOwnerOrReadOnly


class AdoptionList(generics.ListCreateAPIView):
    serializer_class = AdoptionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'advert_id',
        'owner__profile',
    ]
    search_fields = [
        'name',
        'email',
        'mobile',
    ]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Adoption.objects.all()
        return Adoption.objects.none()

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
