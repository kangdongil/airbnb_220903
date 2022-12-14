from django.db import models
from common.models import TimeStampedModel as CommonModel
class Room(CommonModel):

    """Room Model Definition"""

    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRIVATE_ROOM = ("private_room", "Private Room")
        SHARED_ROOM = ("shared_room", "Shared Room")

    name = models.CharField(max_length=180, default="")
    country = models.CharField(max_length=50, default="South Korea")
    city = models.CharField(max_length=50, default="Seoul")
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    address = models.CharField(max_length=250)
    pet_friendly = models.BooleanField(default=True)
    kind = models.CharField(
        max_length=20,
        choices=RoomKindChoices.choices,
    )
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="rooms"
    )
    description = models.TextField(blank=True, null=True)
    amenities = models.ManyToManyField("rooms.Amenity", related_name="rooms")
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.SET_NULL,
        related_name="rooms",
        blank=True,
        null=True,
    )

    def total_amenities(room):
        return room.amenities.count()
    
    def total_reviews(room):
        return room.reviews.count()

    def total_photos(room):
        return room.photos.count()
    
    def rating_average(room):
        count = room.reviews.count()
        if count == 0:
            return 0
        else:
            total_rating = 0;
            for review in room.reviews.all().values("rating"):
                total_rating += review["rating"]
            return round(total_rating / count, 2)
    
    def __str__(self):
        return self.name

class Amenity(CommonModel):

    """Amenity Definition"""

    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Amenities"