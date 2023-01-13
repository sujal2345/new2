from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Type(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class SubType(models.Model):
    name=models.ForeignKey(Type, on_delete=models.CASCADE)
    subty=models.CharField(max_length=200)
    def __str__(self):
        return self.subty


class Post(models.Model):
    address = models.CharField(max_length=700)
    usernames = models.ForeignKey(User, on_delete=models.CASCADE)
    facilities=models.CharField(max_length=800)
    main_image = models.ImageField(null=True, blank=True,upload_to='image/')
    secondary_image = models.ImageField(null=True, blank=True,upload_to="image/")
    third_image = models.ImageField(null=True, blank=True,upload_to="image/")
    type=models.CharField(max_length=100,default='')
    subtype=models.CharField(max_length=100,default='')
    price=models.IntegerField(null=True, blank=True, default=0)
    code=models.CharField(null=True, blank=True, default='1234',max_length=20)
    def __str__(self):
        return str(self.usernames)
    def get_absolute_url(self):
        return reverse('index')
