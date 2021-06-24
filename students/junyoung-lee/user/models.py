from django.db import models

class User(models.Model):
    name        = models.CharField(max_length=50, unique=True)
    nickname    = models.CharField(max_length=50)
    email       = models.EmailField(unique=True)
    phonenumber = models.CharField(max_length=13, unique=True)
    password    = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'users'