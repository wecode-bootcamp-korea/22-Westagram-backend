from django.db import models

class Account(models.Model):
    email           = models.EmailField(max_length=45, unique=True)
    password        = models.CharField(max_length=45)
    nickname        = models.CharField(max_length=45, unique=True)
    phone_number    = models.CharField(max_length=45, unique=True)
    date            = models.DateField(auto_now_add=True)
    update          = models.DateField(auto_now=True)

    class Meta:
        db_table = 'accounts'
