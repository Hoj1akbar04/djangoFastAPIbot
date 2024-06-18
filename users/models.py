from django.db import models
from .helpers import SaveMediaFile


class Users(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)
    username = models.CharField(max_length=40)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"







