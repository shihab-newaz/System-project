from django.db import models
from asyncio.windows_events import NULL
from calendar import c
from email.policy import default
from enum import unique
from random import choices
from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models



class Product(models.Model):
    title=models.CharField(max_length=255) #varchar 255
    processor=models.CharField(max_length=255)
    ram=models.CharField(max_length=255)
    storage=models.CharField(max_length=255)
    display=models.CharField(max_length=255)
    serial_number = models.CharField(max_length=64, unique=True,default=100)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    last_updated =models.DateTimeField(auto_now=True)
    image=models.ImageField(null=True,blank=True,upload_to='images/')
    def __str__(self):
         return self.title
     
class Customer(models.Model):
    first_name=models.CharField(max_length=255,default='Shihab')
    last_name=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=255)
    birth_date=models.DateField(null=True)

    def __str__(self):
         return self.first_name   
     
class Review(models.Model):
    ratingChoices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')]
    review=models.TextField()
    rating=models.CharField(max_length=255,choices=ratingChoices)
    created_at=models.DateTimeField(auto_now_add=True)
    product=models.ForeignKey(Product,on_delete=models.PROTECT)
    sentiment=models.CharField(max_length=255,default=NULL)
    customer=models.CharField(max_length=255,default="")
    def __str__(self):
        return self.rating
     
class Record(models.Model):
    customer=models.CharField(max_length=255,default="")
    bought_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.customer
         

   

 