from django.db import models

# Create your models here.

class Section(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name


class Person(models.Model):
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name