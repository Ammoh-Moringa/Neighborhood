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


