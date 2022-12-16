from django.contrib import admin
from .models import Room, Amenity


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "price",
        "type",
        "owner",
        "updated",
        "created",
    )

    list_filter = (
        "country",
        "city",
        "pet_friendly",
        "type",
        "amenities",
        "updated",
        "created",
    )


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "updated",
        "created",
    )
    readonly_fields = (
        "updated",
        "created",
    )
