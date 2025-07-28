from tokenize import blank_re
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null=True,blank=True)
    phone = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    profile_pic = models.ImageField(null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class Product_item(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Out Door','Out Door')
    )
    name =  models.CharField(max_length=100,null=True,blank=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=100,null=True,blank=True,choices=CATEGORY)
    description =  models.CharField(max_length=100,null=True,blank=True )
    date_created = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
    ('Pending','Pending'),
    ('Out for delivery','Out for delivery'),
    ('Delivered','Delivered')
    )
    customer = models.ForeignKey(Customer, null=True, on_delete = models.SET_NULL)
    product = models.ForeignKey(Product_item, null=True, on_delete = models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    status = models.CharField(max_length=100,null=True,blank=True,choices=STATUS)