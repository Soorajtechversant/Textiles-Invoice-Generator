from django.db import models
import datetime


# # Create your models here.
class seller(models.Model):
    name = models.CharField(max_length=50,default="Soorak kp")
    address = models.CharField(max_length=150,default="Chakkingal, Palakkad")
    phone = models.IntegerField(default='+91 8941525253')
    date = models.DateField(default=datetime.datetime.date)

class buyer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    phone = models.IntegerField()
    purchase_date = models.DateField(default=datetime.datetime.now)

class productz(models.Model):
    img = models.ImageField(upload_to='media/')
    name = models.CharField(max_length=100)
    dis = models.TextField(max_length=500)
    price = models.CharField(max_length=100)

class Billing(models.Model):
    Name = models.CharField(max_length=20)
    Address= models.CharField(max_length=40)
    Phone = models.IntegerField()
    # Price = models.IntegerField()
    Quantity = models.IntegerField()
