from django.db import models

# Create your models here.
class Expense(models.Model):
    expense=models.CharField(max_length=20,null=True)
    amount=models.DecimalField(max_digits=20,decimal_places=5,null=True)
    category=models.CharField(max_length=20,null=True)
    