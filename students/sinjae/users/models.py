from django.db                  import models
from django.db.models.deletion  import CASCADE

class User(models.Model):

    gender_choice = (
        ('male', 'Male')
        ('female', 'Female')
        ('custom', 'Custom')
        ('prefer not to say', 'Prefer Not To Say')
    )

    nick_name       = models.CharField(max_length=20) 
    name            = models.CharField(max_length=40) 
    password        = models.CharField(max_length=200)
    website         = models.CharField(max_length=100, null=True)
    bio             = models.CharField(max_length=100, null=True)
    email           = models.CharField(max_length=100)
    phone_number    = models.CharField(max_length=30) 
    gender          = models.CharField('Gender', max_length=20, choices= gender_choice)
    birth_date      = models.DateField()
    created_at      = models.DateTimeField(auto_now=True, auto_now_add=True)
    
    class Meta:
        db_table    = 'users'
