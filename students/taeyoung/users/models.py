from django.db import models

class Account(models.Model):
    name            = models.CharField(max_length=45)
    email           = models.EmailField(max_length=45, unique=True)
    password        = models.CharField(max_length=200)
    nickname        = models.CharField(max_length=45, unique=True)
    phone_number    = models.CharField(max_length=45, unique=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'accounts'
