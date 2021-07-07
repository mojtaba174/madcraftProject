from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    thumbnail = models.ImageField(default="default-image.jpg", blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.title
