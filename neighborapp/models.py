from django.db import models
from django.contrib.auth.models import  User
# Create your models here.

class Neighbourhood(models.Model):
    neighbourhood_name = models.CharField(max_length=60,blank=False)
    neighbourhood_location = models.CharField(max_length=60,blank=False)
    occupants_count = models.IntegerField()
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='neighbor')



#class profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    nieghborhood_name = models.CharField(max_length=80, blank=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(max_length=254, blank=True)
    profile_picture = models.ImageField(upload_to='images/', default='default.png')
    neighbourhood_id = models.ForeignKey(Neighbourhood, on_delete=models.SET_NULL, null=True, related_name='members', blank=True)

#class Bussiness
class Bussiness(models.Model):
     business_user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='owner')
     name = models.CharField(max_length=120)
     business_email = models.EmailField(max_length=254)
     neighbourhood_id = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='business')
    

   




 


