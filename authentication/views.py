from django.shortcuts import render
from django.http import Http404
from .serializer import UserSerializerClass
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserModel
from django.contrib.auth.models import User


# Create your views here.
class UserRegistrationView(APIView):
    serializer_class = UserSerializerClass
    all_users = User.objects.all()
    model = UserModel
    
    def get_user(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise Http404

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data

        response = {
            'data': {
                "user": dict(user_data),
                "status": "success",
                "message": "Account created successfully"
            }
        }

        return Response(response, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        serializers = UserSerializerClass(self.all_users, many=True)
        return Response(serializers.data)
    
    def post(self, request, format=None, *args, **kwargs):
        serializers = UserSerializerClass(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None, *args, **kwargs):
        user = self.get_user(pk)
        serializers = UserSerializerClass(user, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        user = self.get_user(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

