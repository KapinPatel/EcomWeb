from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Vendor(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.TextField(null=True)

class Product_category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title= models.CharField(max_length=200)
    details= models.TextField(null=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    category=models.ForeignKey(Product_category,on_delete=models.SET_NULL,null=True)
    vendor=models.ForeignKey(Vendor,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=200)
    details=models.TextField(null=True)
    price=models.FloatField()

    def __str__(self):
        return self.title