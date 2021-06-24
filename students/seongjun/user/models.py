from django.db import models


class Account(models.Model):
    email           = models.EmailField(max_length=100)
    password        = models.CharField(max_length=45)
    nick_name       = models.CharField(max_length=45)
    phone_number    = models.CharField(max_length=100)
    register_dttm   = models.DateField(auto_now_add=True)
    update_dttm     = models.DateField(auto_now=True)

    class Meta:
        db_table = 'accounts'
