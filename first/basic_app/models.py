from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class UserProfileInfo(models.Model):

    
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        
        return self.user.username


class YourEnvironment(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("basic_app:list")

class YourPics(models.Model):
    pic_name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='photos/all/',blank=True)
    image_description = models.CharField(max_length=256,blank=True,default="")
    Category = models.ForeignKey(YourEnvironment,related_name='photographer',on_delete=models.CASCADE)

    def __str__(self):
        return self.pic_name

    def get_absolute_url(self):
        return reverse("basic_app:list")