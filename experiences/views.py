from rest_framework.views import APIView
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Perk
from .serializers import PerkSerializer
from common.paginations import ListPagination

class PerkList(APIView, ListPagination):
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        all_perks = Perk.objects.all().order_by("pk")
        serializer = PerkSerializer(
            self.paginate(all_perks, request),
            many=True,
        )
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PerkSerializer(data=request.data)
        if serializer.is_valid():
            new_perk = serializer.save()
            return Response(
            	PerkSerializer(new_perk).data,
            )
        else:
            return Response(serializer.errors)
    
class PerkDetail(APIView):
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_object(self, pk):
        try:
            return Perk.objects.get(pk=pk)
        except Perk.DoesNotExist:
            return NotFound
        
    def get(self, request, pk):
        perk = self.get_object(pk)
        serializer = PerkSerializer(perk)
        return Response(serializer.data)
    
    def put(self, request, pk):
        perk = self.get_object(pk)
        serializer = PerkSerializer(
        	perk,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_perk = serializer.save()
            return Response(
            	PerkSerializer(updated_perk).data,
            )
        else:
            return Response(serializer.errors)
    
    def delete(self, request, pk):
        perk = self.get_object(pk)
        perk.delete()
        return Response(status=HTTP_204_NO_CONTENT)

class ExperiencePhotos(APIView):
    def post(self,request, pk):
        pass

class ExperienceVideos(APIView):
    def post(self,request, pk):
        pass