from django.db import models
from django.db.models import DateField
import datetime



class User(models.Model):
    email = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=128)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField(default=datetime.date.today)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True) 
    joined_at = models.DateTimeField(auto_now_add=True) # yaratilgan vaqt
    language = models.CharField(max_length=30) # til
    country = models.CharField(max_length=100) # davlat
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return self.username