from django.db import models
from common.models import CommonModel
from config.settings import AUTH_USER_MODEL


class Booking(CommonModel):

    """Booking Model Definition"""

    class BookingTypeChoices(models.TextChoices):
        ROOM = ("room", "Room")
        EXPERIENCE = ("experience", "Experience")

    type = models.CharField(
        max_length=15,
        choices=BookingTypeChoices.choices,
    )
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    room = models.ForeignKey(
        "rooms.Room",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    check_in = models.DateField(
        null=True,
        blank=True,
    )
    check_out = models.DateField(
        null=True,
        blank=True,
    )
    experience_time = models.DateTimeField(
        null=True,
        blank=True,
    )
    guests = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.type.title()} booking for: {self.user}"
