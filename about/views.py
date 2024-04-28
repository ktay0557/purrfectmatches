from rest_framework import generics, permissions
from purrfectmatches.permissions import IsStaffOrReadOnly
from .models import About
from .serializers import AboutSerializer


class AboutList(generics.ListAPIView):
    """
    Show users the most up to date About information. 
    """
    serializer_class = AboutSerializer
    permission_classes = [IsStaffOrReadOnly]

    def get_queryset(self):
        return About.objects.order_by('-created_at')

class AboutDetail(generics.RetrieveUpdateAPIView):
    """
    Allows staff to retrieve and update the About information. 
    """
    serializer_class = AboutSerializer
    permission_classes = [IsStaffOrReadOnly]
    queryset = About.objects.all()