from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Restaurants
from .serializers import RestaurantSerializer
from django.shortcuts import get_object_or_404

# Create your views here.

class RestaurantView(APIView):
    def get(self,request): 
        print(request.data) 
     
        serializer=RestaurantSerializer(Restaurants.objects.all(),many=True)
     
        print(serializer.data)
      
        return Response(serializer.data)