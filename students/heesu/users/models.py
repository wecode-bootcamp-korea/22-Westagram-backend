from django.db  import models

class User(models.Model) :
    # Not Nullable Field (Order by Sinup Form's input_Seq)
    phone_nmber     = models.CharField(unique=True,max_length=100,null=False)
    email           = models.EmailField(unique=True,max_length=100,null=False)
    full_name       = models.CharField(max_length=50,null=False)
    password        = models.CharField(max_length=200,null=False)
    nick_name       = models.CharField(max_length=50,null=False)
    # Nullable Field (Do not use when the First SignUp)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    login_at        = models.DateTimeField()
    class Meta :
        db_table    = 'users'