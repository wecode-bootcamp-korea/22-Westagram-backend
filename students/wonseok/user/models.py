from django.db import models

class User(models.Model):
    following     = models.ManyToManyField("User", through="FollowerRelation", related_name="follower")
    email         = models.EmailField(max_length=100,unique=True,)
    password      = models.CharField(max_length=30)
    nick_name     = models.CharField(max_length=100)
    name          = models.CharField(max_length=50)
    phone_number  = models.CharField(max_length=20, unique=True)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "users"

class FollowerRelation(models.Model):
    follower     = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    user         = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower_user")
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "follower_relations"