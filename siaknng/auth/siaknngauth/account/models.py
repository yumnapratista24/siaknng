from django.conf import settings
from django.db import models


class Account(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, models.CASCADE)
    npm = models.CharField(max_length=255)
    faculty_id = models.IntegerField(unique=True)
