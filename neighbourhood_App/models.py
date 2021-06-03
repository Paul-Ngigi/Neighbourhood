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
    
    def save_neighbourhood(self):
        self.save()
        
    def delete_neighbourhood(self):
        self.delete()
    
    @classmethod
    def update_neighbourhood(self, id, neighbourhood_name):
        return Neighbourhood.objects.get(id=id).update(neighbourhood_name=neighbourhood_name)
        

    @classmethod
    def find_by_id(self, id):
        return Neighbourhood.objects.get(pk=id)
    
        
    @classmethod
    def update_count(self, id, count):
        return Neighbourhood.objects.get(id=id).update(count=count)
    