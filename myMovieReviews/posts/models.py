from django.db import models

# Create your models here.
GENRES = (
    ('드라마', '드라마'),
    ('코미디', '코미디'),
    ('스릴러', '스릴러'),
    ('공포', '공포'),
    ('SF', 'SF'),
    ('판타지', '판타지'),
    ('멜로/로맨스', '멜로/로맨스'),
    ('다큐멘터리', '다큐멘터리')
)
class Review(models.Model):
    title = models.CharField(max_length=50)
    release = models.CharField(max_length=10)
    genre = models.CharField(max_length=32, choices=GENRES)
    rating = models.CharField(max_length=10)
    runningTime = models.PositiveIntegerField(null=True, blank=True)
    content = models.TextField()
    director = models.CharField(max_length=32)
    actor = models.CharField(max_length=80)