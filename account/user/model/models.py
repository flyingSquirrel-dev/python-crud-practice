from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=24, unique=True)
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)