from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=3)

    def __str__(self):
        return self.name

class Tracker_User(models.Model):
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.CharField(max_length=3)

    def __str__(self):
        return self.username