from django.db import models
from django.contrib.auth.models import  User
# Create your models here.

class Neighbourhood(models.Model):
    neighbourhood_name = models.CharField(max_length=60,blank=False)
    neighbourhood_location = models.CharField(max_length=60,blank=False)
    occupants_count = models.IntegerField()
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='neighbor')

    def __str__(self):
        return f'{self.neighbourhood_name} neighbor'

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)

    @classmethod
    def update_occupants(cls,neighbourhood_id):
        occupation = cls.objects.get(id=neighbourhood_id)
        new_count = occupation.occupation_count + 1
        cls.objects.filter(id = neighbourhood_id).update(occupation_count = new_count)

    def update_neighborhood(self):
        name = self.name
        self.name = name



#class profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    nieghborhood_name = models.CharField(max_length=80, blank=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(max_length=254, blank=True)
    profile_picture = models.ImageField(upload_to='images/', default='default.png')
    neighbourhood_id = models.ForeignKey(Neighbourhood, on_delete=models.SET_NULL, null=True, related_name='members', blank=True)

    def __str__(self):
        return self.user

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

#class Bussiness
class Bussiness(models.Model):
     business_user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='owner')
     name = models.CharField(max_length=120)
     business_email = models.EmailField(max_length=254)
     neighbourhood_id = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='business')

     def __str__(self):
        return f'{self.name}Business'

     def save_business(self):
        self.save()

     def create_business(self):
            self.save()

     def delete_business(self):
        self.delete()

     @classmethod
     def find_business(cls,business_id):
        business = cls.objects.get(id = business_id)
        return business

     def update_business(self):
        name = self.name
        self.name = name
    

   




 


