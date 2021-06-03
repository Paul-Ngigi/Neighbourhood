from django.urls import path
from .views import Neighbourhood

urlpatterns = [
    path('', Neighbourhood.as_view(), name='neighbourhood')
]
