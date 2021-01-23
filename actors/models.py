from django.db import models


class User(models.Model):
    name = models.CharField(max_length=64)
    password = models.CharField(max_length=32, null=True)
    

class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    

# Create your models here.
