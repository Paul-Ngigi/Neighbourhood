from django.http import response
from django.shortcuts import render
from .serializers import BusinessClass
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class BusinessView(generics.GenericAPIView):
    serializer_class = BusinessClass
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        business_data = serializer.data
        
        response = {
            'data': {
                'business':dict(business_data),
                "status": "success",
                "message": "Business created successfully"
            }
        }
        
        return Response(response, status=status.HTTP_201_CREATED)
        
        