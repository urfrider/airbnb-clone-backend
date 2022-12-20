from django.contrib import admin
from .models import Room, Amenity


@admin.action(description="Set all prices to zero")
def reset_prices(model_admin, request, rooms):
    for room in rooms:
        room.price = 0
        room.save()


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    actions = (reset_prices,)

    list_display = (
        "name",
        "price",
        "type",
        "total_amenities",
        "owner",
        "rating",
        "created",
    )

    list_filter = (
        "country",
        "city",
        "pet_friendly",
        "type",
        "amenities",
        "created",
    )

    search_fields = (
        "name",
        "=price",
        "^owner__username",
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
