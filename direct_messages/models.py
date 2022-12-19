from django.db import models
from common.models import CommonModel
from config.settings import AUTH_USER_MODEL


class ChatRoom(CommonModel):

    """Chat Room Model Definition"""

    users = models.ManyToManyField(
        AUTH_USER_MODEL,
        related_name="chatRooms",
    )

    def __str__(self):
        return "Chat Room"


class Message(CommonModel):

    """Message Model Definition"""

    text = models.TextField()
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="messages",
    )
    chatroom = models.ForeignKey(
        "direct_messages.ChatRoom",
        on_delete=models.CASCADE,
        related_name="messages",
    )

    def __str__(self):
        return f"{self.user} says: {self.text}"
