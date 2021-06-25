from django.db import models

class User(models.Model): 
    email        = models.EmailField(max_length=45, unique=True)
    password     = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=45, unique=True)
    nickname     = models.CharField(max_length=45, unique=True)

    class Meta:
        db_table = 'users'