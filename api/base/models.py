from django.db import models

# Create your models here.
class Advocate(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=500, null=True, blank=True)