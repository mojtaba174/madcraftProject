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
    show = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Comments(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f'comment {self.body} by {self.name}'
