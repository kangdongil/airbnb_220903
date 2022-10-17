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
        
class PublicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
    # 내 리뷰 보기
    # 내 집
    # 내가 여행한 도시
    # 나에 대한 리뷰
        