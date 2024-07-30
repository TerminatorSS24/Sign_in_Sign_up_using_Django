from django.db import models
class Users(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=250)
