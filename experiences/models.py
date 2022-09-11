from django.db import models
from common.models import TimeStampedModel as CommonModel


class Experience(CommonModel):

    """Experience Model Definition"""

    name = models.CharField(max_length=250)
    country = models.CharField(
        max_length=50,
        default="한국",
    )
    city = models.CharField(
        max_length=80,
        default="서울",
    )
    host = models.ForeignKey("users.User", on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    address = models.CharField(max_length=250)
    start = models.TimeField()
    end = models.TimeField()
    description = models.TextField(blank=True, null=True)
    perks = models.ManyToManyField("experiences.Perk")
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name


class Perk(CommonModel):

    """What is included on an Experience"""

    name = models.CharField(max_length=100)
    details = models.CharField(
        max_length=250,
        blank=True,
        default="",
    )
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
