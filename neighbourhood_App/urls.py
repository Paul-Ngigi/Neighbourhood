from django.urls import path
from .views import NeighbourhoodView
from .models import Neighbourhood

urlpatterns = [
    path('', NeighbourhoodView.as_view(queryset=Neighbourhood.objects.all()), name='neighbourhood')
]
