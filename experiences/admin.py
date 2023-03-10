from django.contrib import admin
from .models import Experience, Service


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "price",
        "start",
        "end",
        "created",
    )
    list_filter = ("category",)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "detail",
        "description",
    )
