from django.db import models

class Account(models.Model):
    email           = models.EmailField(max_length=100, unique=True)
    password        = models.CharField(max_length=200)
    nick_name       = models.CharField(max_length=45, unique=True)
    phone_number    = models.CharField(max_length=45, unique=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'accounts'
