from django.db                  import models
from django.db.models.deletion  import CASCADE

class User(models.Model):

    gender_choice = (
        ('male', 'Male')
        ('female', 'Female')
        ('custom', 'Custom')
        ('prefer not to say', 'Prefer Not To Say')
    )

    full_name       = models.CharField(max_length=20) # nick name
    user_name       = models.CharField(max_length=40) 
    password        = models.CharField(max_length=200)
    user_website    = models.CharField(max_length=100, blank=True)
    user_bio        = models.CharField(max_length=100, blank=True)
    email           = models.CharField(max_length=100) # id
    phone_number    = models.CharField(max_length=30) 
    gender          = models.CharField('Gender', max_length=20, choices= gender_choice)
    birth_date      = models.DateField()
    create_date     = models.DateTimeField()
    
    class Meta:
        db_table    = 'users'
