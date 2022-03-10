from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import post_save

class Occupation(models.Model):
    occupation_name = models.CharField(max_length=15)

    def __str__(self):
        return self.occupation_name


class State(models.Model):
    state_name = models.CharField(max_length=25)


    def __str__(self):
        return self.state_name


class TargetArea(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='targetArea')
    state = models.ForeignKey(State,on_delete=models.CASCADE,related_name='targetArea')


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    occupation = models.ForeignKey(Occupation,on_delete=models.CASCADE,related_name='Profile',null=True,blank=True)
    img_profile = models.ImageField(upload_to='profile_img/',null=True,blank=True)
    profile_slug = models.SlugField(blank=True,null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE,null=True,blank=True)




    def get_occupation(self):
        return self.occupation.occupation_name
    def get_absolut_url(self):
        return 'http://127.0.0.1:8000' + self.img_profile.url

    def save(self,*args,**kwargs):
        self.profile_slug = slugify(self.user.username)
        super(Profile,self).save(*args,**kwargs)

class Vehicle(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='vehicle')
    img_vehicle = models.ImageField(upload_to='img_vehicle/')
    img_vehicle_contract = models.ImageField(upload_to='img_vehicle_contract')


    def get_absolut_vehicle_url(self):
        return 'http://127.0.0.1:8000' + self.img_vehicle.url

    def get_absolut_img_vehicle_contract_url(self):
        return 'http://127.0.0.1:8000' + self.img_vehicle_contract.url



class VehicleType(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='vehicle_type')
    type = models.CharField(max_length=50)


class UseVehicleType(models.Model):
    vehicle_type = models.ForeignKey(VehicleType,on_delete=models.CASCADE,related_name='use_vehicle_type')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='use_vehicle_type')




def create_profile(sender, **kwarg):
    print("====================================================")
    if kwarg['created']:
        Profile.objects.create(user=kwarg['instance'])


post_save.connect(create_profile, sender=User)