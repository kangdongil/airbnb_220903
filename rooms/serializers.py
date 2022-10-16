from rest_framework.serializers import ModelSerializer, SerializerMethodField
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer
from medias.serializers import PhotoSerializer
from .models import Room, Amenity
from wishlists.models import Wishlist

class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = "__all__"


class RoomListSerializer(ModelSerializer):
    
    # photos = PhotoSerializer(read_only=True, many=True)
    
    rating = SerializerMethodField()
    
    class Meta:
        model = Room
        fields = ("pk", "name", "country", "city", "price", "rating")

    def get_rating(self, room):
        return room.rating_average()

class RoomDetailSerializer(ModelSerializer):
    
    owner = TinyUserSerializer(read_only=True)
    # amenities = AmenitySerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True)
    # photos = PhotoSerializer(read_only=True, many=True)
    
    rating = SerializerMethodField()
    is_owner = SerializerMethodField()
    is_liked = SerializerMethodField()
    total_reviews = SerializerMethodField()
    total_amenities = SerializerMethodField()
    total_photos = SerializerMethodField()
    
    class Meta:
        model = Room
        exclude = ("amenities",)
    
    def get_rating(self, room):
        return room.rating_average()
    
    def get_is_owner(self, room):
        request = self.context["request"]
        return room.owner == request.user
    
    def get_is_liked(self, room):
        request = self.context["request"]
        return Wishlist.objects.filter(owner=request.user, rooms__pk=room.pk).exists()
    
    def get_total_reviews(self, room):
        return room.total_reviews()
    
    def get_total_amenities(self, room):
        return room.total_amenities()
    
    def get_total_photos(self, room):
        return room.total_photos()