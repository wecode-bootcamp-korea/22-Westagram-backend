
from django.db                    import models

class User(models.Model):
    user_phonenumber = models.CharField(max_length=30)
    user_email       = models.EmailField(max_length=50)
    user_name        = models.CharField(max_length=30)
    user_nickname    = models.CharField(max_length=30)
    user_password    = models.CharField(max_length=50)

    class Meta:
        db_table = 'users'
