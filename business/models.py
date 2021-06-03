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
    
    def save_business(self):
        self.save()
        
    def delete_business(self):
        self.delete()
    
    @classmethod
    def update_business(self, id, business_name):
        return BusinessModel.objects.get(id=id).update(business_name=business_name)
        

    @classmethod
    def find_by_id(self, id):
        return BusinessModel.objects.get(id=id)
    
        
    @classmethod
    def update_count(self, id, business_name):
        return BusinessModel.objects.get(id=id).update(business_email=business_name)
    

