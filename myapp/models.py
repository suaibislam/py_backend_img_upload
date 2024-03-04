from django.db import models
from datetime import datetime

# Create your models here.
class Student(models.Model):
        name=models.CharField(max_length=25,blank=False,null=False)
        datetime = models.DateTimeField(default=datetime.now, blank=True)
        
class Image(models.Model):
 photo = models.ImageField(upload_to="myimage")
 date = models.DateTimeField(auto_now_add=True)        