from django.db import models
from common.models import CommonModel


class Photo(CommonModel):

    """Photo Model Definition for Room / Experience"""

    file = models.ImageField()
    description = models.CharField(
        max_length=150,
        null=True,
        blank=True,
    )
    room = models.ForeignKey(
        "rooms.Room",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return "Photo File"


class Video(CommonModel):

    """Video Model Definition for Experience"""

    file = models.FileField()
    experience = models.OneToOneField(
        "experiences.Experience",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "Video File"
