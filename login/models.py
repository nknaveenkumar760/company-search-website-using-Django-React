from django.db import models

# Create your models here.

class LoginPage(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.CharField(max_length=400)
    password = models.CharField(max_length=400)
    confirm_password = models.CharField(max_length=400)
    nickname = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=15)
    
    