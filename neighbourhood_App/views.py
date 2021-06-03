from django.http import response, Http404, HttpResponse
from django.shortcuts import render
from .serializers import NeighbourhoodClass
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Neighbourhood


# Create your views here.

class NeighbourhoodView(APIView):
    serializer_class = NeighbourhoodClass
    all_neighbourhoods = Neighbourhood.objects.all()
    
    
    def get_object(self, id):
        try:
            return Neighbourhood.objects.get(id=id)
        except Neighbourhood.DoesNotExist as e:
            return Response( {"error": "Given question object not found."}, status=404)

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

    
    def delete(self, request, id=None):
        instance = self.get_object(id)
        instance.delete()
        return HttpResponse(status=204)
    
    def put(self, request, id):
        data = request.data
        instance = self.get_object(id)
        serializer = NeighbourhoodClass(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.erros, status=400)
    
        

        
    