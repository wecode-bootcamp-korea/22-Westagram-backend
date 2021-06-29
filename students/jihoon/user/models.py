from django.db import models

class Account(models.Model):
    name            = models.CharField(max_length=50)
    nickname        = models.CharField(max_length=50, unique=True)
    phone_number    = models.CharField(max_length=50, unique=True)
    password        = models.CharField(max_length=200)
    email           = models.EmailField(max_length=200, unique=True)

    class Meta:
        db_table = "accounts"