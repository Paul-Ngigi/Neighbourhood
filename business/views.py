from django.db import models
from django.http import response, Http404
from django.shortcuts import render
from .serializers import BusinessClass
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import BusinessModel


# Create your views here.
class BusinessView(APIView):
    serializer_class = BusinessClass
    all_business = BusinessModel.objects.all()
    model = BusinessModel
    
    def get_business(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            return Http404

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        business_data = serializer.data

        response = {
            'data': {
                'business': dict(business_data),
                "status": "success",
                "message": "Business created successfully"
            }
        }

        return Response(response, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        serializers = BusinessClass(self.all_business, many=True)
        return Response(serializers.data)

    def put(self, request, pk, format=None, *args, **kwargs):
        business = self.get_business(pk)
        serializers = BusinessClass(business, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        business = self.get_business(pk)
        business.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
