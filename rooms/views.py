from django.db import transaction
from rest_framework.views import APIView
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, NotAuthenticated, ParseError, PermissionDenied
from common.paginations import ListPagination
from categories.models import Category
from .models import Room, Amenity
from .serializers import AmenitySerializer, RoomListSerializer, RoomDetailSerializer

class AmenityList(APIView, ListPagination):
    def get(self, request):
        all_amenities = Amenity.objects.all().order_by("pk")
        serializer = AmenitySerializer(
            self.paginate(all_amenities, request),
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = AmenitySerializer(data=request.data)
        if serializer.is_valid():
            amenity = serializer.save()
            serializer = AmenitySerializer(amenity)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class AmenityDetail(APIView):
    def get_object(self, pk):
        try:
            return Amenity.objects.get(pk=pk)
        except Amenity.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        amenity = self.get_object(pk)
        serializer = AmenitySerializer(amenity)
        return Response(serializer.data)

    def put(self, request, pk):
        amenity = self.get_object(pk)
        serializer = AmenitySerializer(
            amenity,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_amenity = serializer.save()
            return Response(AmenitySerializer(updated_amenity).data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        amenity = self.get_object(pk)
        amenity.delete()
        return Response(status=HTTP_204_NO_CONTENT)

class RoomList(APIView, ListPagination):
    def get(self, request):
        all_rooms = Room.objects.all().order_by("pk")
        serializer = RoomListSerializer(
        	self.paginate(all_rooms, request),
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)
        
    def post(self, request):
        if not request.user.is_authenticated:
            raise NotAuthenticated
        serializer = RoomDetailSerializer(data=request.data)
        if serializer.is_valid():
            category_pk = request.data.get("category")
            amenity_pks = request.data.get("amenities")
            if not category_pk:
                raise ParseError("Category is required.")
            try:
                category = Category.objects.get(pk=category_pk)
                if category.kind != Category.CategoryKindChoices.ROOM:
                    raise ParseError("The category's kind should be 'rooms'.")
            except Category.DoesNotExist:
                raise ParseError("Category not found.")
            try:
                with transaction.atomic():
                    new_room = serializer.save(
                        owner=request.user,
                        category=category,
                    )
                    if amenity_pks:
                        for amenity_pk in amenity_pks:
                            amenity = Amenity.objects.get(pk=amenity_pk)
                            new_room.amenities.add(amenity)
            except Exception:
                raise ParseError("Amenity Not Found")
            serializer = RoomDetailSerializer(new_room)
            return Response(serializer.data)
    
class RoomDetail(APIView, ListPagination):
    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        room = self.get_object(pk)
        serializer = RoomDetailSerializer(
            room,
            context={"request": request},
        )
        return Response(serializer.data)
    
    def put(self, request, pk):
        room = self.get_object(pk)
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if room.owner != request.user:
            raise PermissionDenied
        serializer = RoomDetailSerializer(
        	room,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            category_pk = request.data.get("category")
            amenities = request.data.get("amenities")
            if category_pk:
                try:
                    category = Category.objects.get(pk=category_pk)
                    if category.kind != Category.CategoryKindchoices.ROOM:
                        raise ParseError("The category's kind should be 'rooms'.")
                except Category.DoesNotExist:
                        raise ParseError("Category not Found.")
            try:
                with transaction.atomic():
                    if category_pk:
                        updated_room = serializer.save(category=category)
                    else:
                        updated_room = serializer.save()
                    if amenities:
                        updated_room.amenities.clear()
                        if len(amenities) > 0:
                            for amenity_pk in amenities:
                                amenity = Amenity.objects.get(pk=amenity_pk)
                                updated_room.amenities.add(amenity)
            except Amenity.DoesNotExist:
                raise ParseError("Amenity Not Found")
            except Exception as e:
                raise ParseError(e)
                
            serializer = RoomDetailSerializer(
                updated_room,
                context={"request": request},
            )
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def delete(self, request, pk):
        room = self.get_object(pk)
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if room.owner != request.user:
            raise PermissionDenied
        room.delete()
        return Response(status=HTTP_204_NO_CONTENT)