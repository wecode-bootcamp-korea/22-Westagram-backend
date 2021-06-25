from django.db  import models

class User(models.Model) :
    phone_number    = models.CharField(unique=True,max_length=30)
    email           = models.EmailField(unique=True,max_length=30)
    full_name       = models.CharField(max_length=45)
    password        = models.CharField(max_length=200)
    nick_name       = models.CharField(max_length=30)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    login_at        = models.DateTimeField()
    class Meta :
        db_table    = 'users'