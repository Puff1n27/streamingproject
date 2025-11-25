
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    poster = models.ImageField(upload_to='posters/')
    year = models.IntegerField(default=2025)
    link=models.URLField(blank=True)

    def __str__(self):
        return self.title
    
class Movie2(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    poster = models.ImageField(upload_to='Movie2Poster/')
    year = models.IntegerField(default=2025)
    link=models.URLField(blank=True)
# Create your models here.

class Upcoming(models.Model):
    poster=models.ImageField(upload_to='upcoming/')
    description = models.TextField(blank=True)
    link=models.URLField(blank=True)
