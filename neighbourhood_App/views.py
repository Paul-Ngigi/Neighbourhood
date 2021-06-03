from django.http import response
from django.shortcuts import render
from .serializers import NeighbourhoodClass
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Neighbourhood


# Create your views here.

class NeighbourhoodView(generics.GenericAPIView):
    serializer_class = NeighbourhoodClass
    all_neighbourhoods = Neighbourhood.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        neighbourhood_data = serializer.data

        response = {
            'data': {
                'neighbourhood': dict(neighbourhood_data),
                "status": "success",
                "message": "Neighbourhood created successfully"
            }
        }

        return Response(response, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        serializers = NeighbourhoodClass(self.all_neighbourhoods, many=True)
        return Response(serializers.data)
