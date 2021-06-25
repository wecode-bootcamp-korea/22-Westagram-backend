from datetime   import datetime
from django.db  import models

class USER(models.Model) :
    # Not Nullable Field (Order by Sinup Form's input_Seq)
    phone_nmber     = models.CharField(unique=True,max_length=100,null=False)   # Instagram's Phone Number(Unique)
    email           = models.EmailField(unique=True,max_length=100,null=False)  # Instagram's Email(Unique)
    full_name       = models.CharField(max_length=50,null=False,default='')     # Instagram's Full Name
    password        = models.CharField(max_length=200,null=False)               # Instagram's Password
    nick_name       = models.CharField(max_length=50,null=False,default='')     # Instagram's Username
    # Nullable Field (Do not use when the First SignUp)
    created_at      = models.DateTimeField(default=datetime.now)                # insert current_time when first input
    updated_at      = models.DateTimeField(default=datetime.now)                # insert current_time when update user's infomation
    login_at        = models.DateTimeField(null=True)                           # insert current_time when login sucess
    class Meta :
        db_table    = 'users'