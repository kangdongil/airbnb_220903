from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from . import serializers

class Me(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        serializer = serializers.PrivateUserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request):
        user = request.user
        serializer = serializers.PrivateUserSerializer(
        	user,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            new_user = serializer.save()
            serializer = serializers.PrivateUserSerializer(new_user)
            return Response(serializer.data)
        else:
            return Response(serializers.errors)