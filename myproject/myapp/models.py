from django.db import models
from django.conf import settings

#database

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    username = models.TextField

    def __str__(self):
        return self.username

    