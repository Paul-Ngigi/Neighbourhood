from django.urls import path
from .views import UserRegistrationView
from django.contrib.auth.models import User

urlpatterns = [
    path('register/', UserRegistrationView.as_view(queryset=User.objects.all()), name='register'),
]
