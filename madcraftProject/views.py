from django.shortcuts import render
from articles import models


def Home(request):
    articles = models.Article.objects.all().order_by('-date')
    return render(request, "home.html", {'articles': articles})