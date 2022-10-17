from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from common.paginations import ListPagination
from .models import Wishlist
from .serializers import WishlistSerializer
from rooms.models import Room
from rooms.serializers import RoomListSerializer

class WishlistList(APIView, ListPagination):
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        owned_wishlists = Wishlist.objects.filter(owner=request.user)
        serializer = WishlistSerializer(
        	self.paginate(owned_wishlists, request),
            many=True,
        )
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WishlistSerializer(data=request.data)
        if serializer.is_valid():
            wishlist = serializer.save(
            	owner=request.user,
            )
            serializer = WishlistSerializer(wishlist)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class WishlistDetail(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get_object(self, pk, user):
        try:
            return Wishlist.objects.get(pk=pk, owner=user)
        except Wishlist.DoesNotExist:
            return NotFound
    
    def get(self, request, pk):
        wishlist = self.get_object(pk, request.user)
        serializer = WishlistSerializer(wishlist)
        return Response(serializer.data)
    def put(self, request, pk):
        wishlist = self.get_object(pk, request.user)
        serializer = WishlistSerializer(wishlist, data=request.data, partial=True,)
        if serializer.is_valid():
            updated_wishlist = serializer.save()
            serializer = WishlistSerializer(updated_wishlist)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def delete(self, request, pk):
        wishlist = self.get_object(pk, request.user)
        wishlist.delete()
        return Response(status=HTTP_204_NO_CONTENT)
    
class WishlistToggle(APIView):
    
    def get_list(self, pk, user):
        try:
            return Wishlist.objects.get(pk=pk, owner=user)
        except Wishlist.DoesNotExist:
            raise NotFound
    
    def get_room(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound
    
    def put(self, request, pk, room_pk):
        wishlist = self.get_list(pk, request.user)
        room = self.get_room(room_pk)
        if wishlist.rooms.filter(pk=room.pk).exists():
            wishlist.rooms.remove(room_pk)
            return Response(status=HTTP_204_NO_CONTENT)
        else:
            wishlist.rooms.add(room)
            return Response(status=HTTP_200_OK)
        
            