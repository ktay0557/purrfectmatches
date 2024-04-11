from rest_framework import generics, permissions
from purrfectmatches.permissions import IsStaffOrReadOnly
from .models import About
from .serializers import AboutSerializer


class AboutList(generics.ListAPIView):
    serializer_class = AboutSerializer
    permission_classes = [IsStaffOrReadOnly]

    def get_queryset(self):
        return About.objects.order_by('-created_at')

class AboutDetail(generics.RetrieveUpdateAPIView):
    serializer_class = AboutSerializer
    permission_classes = [IsStaffOrReadOnly]
    queryset = About.objects.all()