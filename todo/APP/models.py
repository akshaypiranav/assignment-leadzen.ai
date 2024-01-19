from django.db import models
from datetime import datetime
# Create your models here.
class Todo(models.Model):
    todo=models.CharField(max_length=10,null=True)
    decription=models.CharField(max_length=100,null=True)
    date=models.CharField(default=datetime.today,max_length=20)
    