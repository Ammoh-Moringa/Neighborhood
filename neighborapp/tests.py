from django.test import TestCase

from django.test import TestCase
from .models import Neighbourhood, Profile
from django.contrib.auth.models import User


# Create your tests here.
class ProfileTestClass(TestCase):

 def setUp(self):
    self.user = User(username="Amos", password="Amo24")
    self.user.save()
    self.neighbourhood= Neighbourhood(hood_name = "8town", hood_location= "kibich", admin = self.user,hood_description='olympic')
    self.neighbourhood.save()
    self.profile = Profile(bio='my hood',email='email@g.com', idNo='678',user = self.user, neighbourhood = self.neighbourhood)

 def test_instance(self):
     self.assertTrue(isinstance(self.profile,Profile))

 def test_save_method(self):
    self.profile.save_profile()
    testsaved = Profile.objects.all()
    self.assertTrue(len(testsaved) > 0)

 def test_delete_method(self):
   self.profile.save_profile()
   testsaved = Profile.objects.all()
   self.assertTrue(len(testsaved) > 0)



class NeighbourhoodTestClass(TestCase):
#Set up Method
  def setUp(self):
  
   self.user = User(username='Amos')
   self.user.save()
   self.neighbourhood = Neighbourhood(neighbourhood_name='Rosya',neighbourhood_location='Nairobi',neighbourhood_description="hood of hoods",neighbourhood_photo='photo.url',admin = self.user)
   self.neighbourhood.create_neighbourhood()


  def tearDown(self):
    Neighbourhood.objects.all().delete()

  def test_instance(self):
    self.assertTrue(isinstance(self.neighbourhood,Neighbourhood))

  def test_create_neighborhood(self):
    self.neighbourhood.create_neighbourhood()
    hoods = Neighbourhood.objects.all()
    self.assertTrue(len(hoods) > 0)

  def test_delete_neighborhood(self):
   self.neighbourhood.create_neighbourhood()
   self.neighbourhood.delete_neighbourhood()
   hood = Neighbourhood.objects.all()
   self.assertTrue(len(hood) == 0)


