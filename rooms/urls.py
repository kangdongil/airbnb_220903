from django.urls import path
from . import views

urlpatterns = [
    path("amenities/", views.AmenityList.as_view()),
    path("amenities/<int:pk>/", views.AmenityDetail.as_view())
]