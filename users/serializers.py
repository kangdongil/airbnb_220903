from rest_framework import serializers
from .models import User

class TinyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
        	"name",
            "avatar",
        )
        
class PrivateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = (
        	"id",
            "password",
            "is_superuser",
            "is_staff",
            "is_active",
            "first_name",
            "last_name",
            "groups",
            "user_permissions",
        )