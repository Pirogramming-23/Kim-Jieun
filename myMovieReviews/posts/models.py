from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=50)
    release = models.CharField(max_length=10)
    genre = models.CharField(max_length=32)
    rating = models.CharField(max_length=10)
    runningTime = models.CharField(max_length=10)
    content = models.TextField()
    director = models.CharField(max_length=32)
    actor = models.CharField(max_length=80)