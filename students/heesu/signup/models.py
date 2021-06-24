from django.db import models


# 사용자 로그인 필수 정보
class USER(models.Model):
    password = models.CharField(max_length=1024)
    email = models.CharField(max_length=45)
    mobile_number = models.CharField(max_length=45)
    nick_name = models.CharField(max_length=45)
    class Meta:
        db_table = 'users'


# 사용자 추가 정보
class USERINFO(models.Model):
    user = models.ForeignKey(USER, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    create_time = models.DateField(null=True)
    update_time = models.DateField(null=True)
    login_time = models.DateField(null=True)
    class Meta:
        db_table = 'users_info'
