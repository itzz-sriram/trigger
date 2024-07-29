from django.db import models

# Create your models here.
class contect(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=30)
    mobile = models.IntegerField()
    city = models.CharField(max_length=60,blank=True)
    course = models.CharField(max_length=30,blank=False)
    batch = models.IntegerField()