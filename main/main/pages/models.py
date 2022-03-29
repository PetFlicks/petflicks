from pyexpat import model
from django.db import models

# Create your models here.


class Post(models):# model for the DB table for post cw
    #followers = ?
    #favorites = ?
    #host =?
    #topic =?
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name