from django.contrib import admin
from .models import ChatRoom, Message


@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "updated",
        "created",
    )
    list_filter = ("created",)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "text",
        "user",
        "chatroom",
        "created",
    )
    list_filter = ("created",)
