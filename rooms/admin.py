from django.contrib import admin
from .models import Room, Amenity
from .actions import reset_prices

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
          
    actions = (reset_prices,)
          
    list_display = (
        "name",
        "price",
        "kind",
        "total_amenities",
        "rating_average",
        "owner",
        "created_at",
    )

    list_filter = (
        "country",
        "city",
        "price",
        "rooms",
        "toilets",
        "pet_friendly",
        "kind",
        "amenities",
    )
    search_fields = (
    	"name",
        "=owner__username",
    )
    search_help_text = "First by Room Name, Second by Owner Name"
    
@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "created_at",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
