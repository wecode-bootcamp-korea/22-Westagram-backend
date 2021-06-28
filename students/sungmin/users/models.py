from django.db import models

class User(models.Model):
        email           = models.EmailField(max_length=100, unique=True)
        nick_name       = models.CharField(max_length=50, unique=True)
        password        = models.CharField(max_length=200)
        phonenumber     = models.CharField(max_length=50)
        created_at      = models.DateTimeField(auto_now_add=True)
        updated_at      = models.DateTimeField(auto_now=True)

        class Meta:
            db_table = 'users'

