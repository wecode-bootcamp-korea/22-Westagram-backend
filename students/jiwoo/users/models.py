from django.db import models

class User(models.Model): 
    email        = models.EmailField(unique=True)
    password     = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20, unique=True)
    name         = models.CharField(max_length=30, unique=True)

    class Meta: 
        db_table = 'users'
