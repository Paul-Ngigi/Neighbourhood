from django.urls import path
from .views import BusinessView

# App urls
urlpatterns = [
    path('', BusinessView.as_view()),
    path('<int:pk>/', BusinessView.as_view()),
    path('update/<int:pk>/', BusinessView.as_view()),
    path('delete/<int:pk>/', BusinessView.as_view())
]
