from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length = 40)
    password = models.CharField(max_length = 40)

    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    last_login_time = models.DateTimeField()

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = 'users'
        db_table = 'user_info'
