from django.contrib import admin
from .models import Review
from .filters import PopularityFilter



@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    
    list_display = (
        "__str__",
        "payload",
    )
    list_filter = (
        PopularityFilter,
    	"rating",
        "user__is_host",
        "room__category",
        "room__pet_friendly",
    )