from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Neighbourhood(models.Model):
    neighbourhood_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    count = models.IntegerField(null=False)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.neighbourhood_name
