from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    revenue = models.DecimalField(max_digits=20, decimal_places=2)
    country = models.CharField(max_length=60)
    techstack = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")