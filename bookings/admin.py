from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "type",
        "user",
        "room",
        "experience",
        "check_in",
        "check_out",
        "experience_time",
        "guests",
    )
    list_filter = ("type",)
