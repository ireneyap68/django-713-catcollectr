from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CatToy(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.name
        
class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    age = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cattoys = models.ManyToManyField(CatToy)

    def __str__(self):
        return self.name

class videos(models.Model):
    video_id = models.CharField(blank=False, max_length=32)
    file_name = models.CharField(blank=False, max_length=500)
    def __str__(self):
        return self.video_id