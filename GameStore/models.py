from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    phone = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True,blank=True)