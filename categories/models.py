from django.db import models
from common.models import CommonModel


class Category(CommonModel):

    """Room / Expereince Category Model"""

    class CategoryTypeChoices(models.TextChoices):
        ROOMS = (
            "rooms",
            "Rooms",
        )
        Experiences = (
            "experiences",
            "Experiences",
        )

    name = models.CharField(
        max_length=50,
    )
    type = models.CharField(
        max_length=15,
        choices=CategoryTypeChoices.choices,
    )

    def __str__(self):
        return f"{self.type.title()}: {self.name}"

    class Meta:
        verbose_name_plural = "Categories"
