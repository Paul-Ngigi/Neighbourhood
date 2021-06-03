from django.db import models
from django.contrib.auth.models import User
from neighbourhood_App.models import Neighbourhood


# Create your models here.
class BusinessModel(models.Model):
    business_name = models.CharField(max_length=100)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    business_email = models.EmailField()
    
    def __str__(self) -> str:
        return self.business_name

