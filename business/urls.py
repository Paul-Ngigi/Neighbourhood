from django.urls import path
from .views import BusinessView
from .models import BusinessModel

urlpatterns = [
    path('', BusinessView.as_view(), name='business'),
]
    

