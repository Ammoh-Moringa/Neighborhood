from django.test import TestCase

from django.test import TestCase
from .models import Neighbourhood, Profile
from django.contrib.auth.models import User


# Create your tests here.
class ProfileTestClass(TestCase):
# Set up method
 def setUp(self):
    self.user = User(username="juma.a", password="pass123")
    self.user.save()
    self.neighbourhood= Neighbourhood(hood_name = "route4", hood_location= "Eastside", admin = self.user,hood_description='mtaa yetu')
    self.neighbourhood.save()
    self.profile = Profile(bio='my hood',email='email@g.com', id_number=3677093,user = self.user, neighbourhood = self.neighbourhood)

 def test_instance(self):
     self.assertTrue(isinstance(self.profile,Profile))

 def test_save_method(self):
    self.profile.save_profile()
    testsaved = Profile.objects.all()
    self.assertTrue(len(testsaved) > 0)

 def test_get_profile(self):
   self.profile.save_profile()
   profile = Profile.get_profile()
   self.assertTrue(len(profile) > 0)


def test_delete_method(self):
  self.profile.save_profile()
  testsaved = Profile.objects.all()
  self.assertTrue(len(testsaved) > 0)


