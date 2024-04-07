from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Adverts
from .serializers import AdvertSerializer
from purrfectmatches.permissions import IsOwnerOrReadOnly


class AdvertList(APIView):
    serializer_class = AdvertSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        adverts = Adverts.objects.all()
        serializer = AdvertSerializer(
            adverts, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = AdvertSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

class AdvertDetail(APIView):
    """
    Retrieve and edit adverts using advert IDs
    """
    serializer_class = AdvertSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            advert = Adverts.objects.get(pk=pk)
            self.check_object_permissions(self.request, advert)
            return advert
        except Adverts.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        advert = self.get_object(pk)
        serializer = AdvertSerializer(
            advert, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        advert = self.get_object(pk)
        serializer = AdvertSerializer(
            advert, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        advert = self.get_object(pk)
        advert.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )