from django.db import models

class User(models.Model): 
    email        = models.EmailField()
    password     = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    name         = models.CharField(max_length=30)
    
    class Meta: 
        db_table = 'users'
