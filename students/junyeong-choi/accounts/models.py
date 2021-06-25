from django.db import models
from django.db.models.fields import EmailField

class Account(models.Model):
    email           = models.EmailField(unique=True, max_length=80)
    password        = models.CharField(max_length=200)
    nickname        = models.CharField(max_length=30)
    phone_number    = models.IntegerField(unique=True, max_length=20)

    class Meta:
        db_table    = "accounts"
