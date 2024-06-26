from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import PermissionDenied
from purrfectmatches.permissions import IsStaffOrReadOnly
from .models import Adverts
from .serializers import AdvertSerializer


class AdvertList(generics.ListCreateAPIView):
    """
    List adverts, or if staff, can create a advert.
    The perform_create method associates the advert with the logged in staff member. 
    """
    serializer_class = AdvertSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Adverts.objects.annotate(
        likes_count=Count('likes', distinct=True), 
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'likes__owner__profile',
        'owner__profile',
    ]
    search_fields = [
        'title',
        'name',
        'age',
        'breed',
        'sex',
        'children',
        'other_animals',
    ]
    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_at',
    ]

    def perform_create(self, serializer):
        if not self.request.user.is_staff:
            raise PermissionDenied(
                "You do not have access"
            )
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
