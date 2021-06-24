import re
from django.db import models
from django.core.validators import EmailValidator, MinLengthValidator


email_regex = re.compile(
    r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*"  # dot-atom
    r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-\011\013\014\016-\177])*"'
    r")@((?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)$)"  # domain
    r"|\[(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}\]$"
)


class User(models.Model):
    email = models.CharField(max_length=50, validators=[EmailValidator(email_regex)])
    password = models.CharField(
        max_length=30, validators=[MinLengthValidator(limit_value=8)]
    )
    phone_number = models.IntegerField(null=True, unique=True)
    nick_name = models.CharField(max_length=100, unique=True, null=True)

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.nick_name
