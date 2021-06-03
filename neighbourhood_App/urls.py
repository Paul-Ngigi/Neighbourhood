from django.urls import path
from .views import NeighbourhoodView
from .models import Neighbourhood

urlpatterns = [
    path('', NeighbourhoodView.as_view(), name='neighbourhood'),
    path('<int:id>/delete/', NeighbourhoodView.as_view(), name='delete_neighbourhood'),
    path('<int:id>/update/', NeighbourhoodView.as_view(), name='update_neighbourhood')
]
