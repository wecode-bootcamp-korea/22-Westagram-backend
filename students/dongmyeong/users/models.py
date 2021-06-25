from django.db import models

class User(models.Model):
    email    = models.CharField(max_length=320, unique=True)
    password = models.CharField(max_length=100)
    phone    = models.IntegerField(unique=True)
    nickname = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return ', '.join([self.id, self.email, self.password, self.phone, self.nickname])
