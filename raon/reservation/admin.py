from django.contrib import admin

# Register your models here.
from . import models


@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
        'date',
        'phonenumber',
        'status',
    )
    list_display = (
        'name',
        'phonenumber',
        'date',
        'package',
        'status',
    )

