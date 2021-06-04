from django.urls import path
from .views import UserRegistrationView

# App urls
urlpatterns = [
    path('', UserRegistrationView.as_view()),
    path('<int:pk>/', UserRegistrationView.as_view()),
    path('update/<int:pk>/', UserRegistrationView.as_view()),
    path('delete/<int:pk>/', UserRegistrationView.as_view())
]
