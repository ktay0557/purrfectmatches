from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Adoption
from .serializers import AdoptionSerializer
from purrfectmatches.permissions import IsStaffOrReadOnly


class AdoptionList(generics.ListCreateAPIView):
    """
    List completed adoption queries,
    or complete adoption queries if logged in. 
    """
    serializer_class = AdoptionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Adoption.objects.all()
    filter_backends = [
        filters.SearchFilter,
    ]
    search_fields = [
        'name',
        'email',
        'mobile',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class AdoptionDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve and delete adoption queries using adoption IDs
    """
    serializer_class = AdoptionSerializer
    permission_classes = [IsStaffOrReadOnly]
    queryset = Adoption.objects.all()
