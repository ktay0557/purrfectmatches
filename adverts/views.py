from django.db.models import Count
from rest_framework import generics, permissions, filters
from purrfectmatches.permissions import IsStaffOrReadOnly
from .models import Adverts
from .serializers import AdvertSerializer


class AdvertList(generics.ListCreateAPIView):
    serializer_class = AdvertSerializer
    permission_classes = [IsStaffOrReadOnly]
    queryset = Adverts.objects.annotate(
        likes_count=Count('likes', distinct=True), 
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
class AdvertDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve and edit adverts using advert IDs
    """
    serializer_class = AdvertSerializer
    permission_classes = [IsStaffOrReadOnly]
    queryset = Adverts.objects.annotate(
        likes_count=Count('likes', distinct=True), 
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
