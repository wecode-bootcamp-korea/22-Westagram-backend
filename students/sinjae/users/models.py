from django.db                  import models
from django.db.models.deletion  import CASCADE

class User(models.Model):

    class Meta:
        db_table    = 'users'
