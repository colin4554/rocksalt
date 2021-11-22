from django.db import models


class Vehicle(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='upload/')
    name = models.CharField(max_length=50)