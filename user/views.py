from django.shortcuts import render
from .serializer import UserSerializerClass
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class UserRegistrationView(generics.GenericAPIView):
    serializer_class = UserSerializerClass

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


