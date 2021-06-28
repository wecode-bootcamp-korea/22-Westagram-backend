from django.db import models
from django.db.models.fields import EmailField

class User(models.Model):
    name         = models.CharField(max_length=20)
    password     = models.CharField(max_length=200)
    email        = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    nickname     = models.CharField(max_length=50, unique=True)
    
    
    class Meta:
        db_table = 'users'