from rest_framework import serializers
from . import models

class DetailReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reservation
        fields = (
            'date',
            'package',
            'name',
            'headcount',
            'others',
            'phonenumber',
            'status',
        )

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reservation
        fields = (
            'date',
            'package',
            'name',
            'headcount',
            'others',
            'phonenumber',
        )