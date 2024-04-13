from rest_framework import generics, permissions
from purrfectmatches.permissions import IsStaffOrReadOnly
from .models import Adverts
from .serializers import AdvertSerializer


class AdvertList(generics.ListCreateAPIView):
    serializer_class = AdvertSerializer
    permission_classes = [IsStaffOrReadOnly]
    queryset = Adverts.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
class AdvertDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve and edit adverts using advert IDs
    """
    serializer_class = AdvertSerializer
    permission_classes = [IsStaffOrReadOnly]
    queryset = Adverts.objects.all()
