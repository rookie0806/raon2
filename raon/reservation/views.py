from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers
from rest_framework.permissions import AllowAny

class NameSearch(APIView):

    def get(self, request, format=None):

        name_search = request.query_params.get('name_search', None)
        if name_search is not None:
            reservation = models.Reservation.objects.filter(name__contains=name_search)
            serializer = serializers.DetailReservationSerializer(reservation, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class Reservation(APIView):
    def post(self, request, format=None):
        serializer = serializers.ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)