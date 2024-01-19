from django.db import models

# Create your models here.
class City(models.Model):
    Cname=models.CharField(max_length=20,blank=True, null=True)
