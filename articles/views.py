from django.shortcuts import render, redirect, HttpResponse
from . import forms
from django.contrib.auth.decorators import login_required
from . import models


@login_required(login_url="/users/login")
def CreateArticle(request):
    if request.method == "POST":
        form = forms.CreateNewArticle(request.POST, request.FILES)
        if form.is_valid():
            formInstance = form.save(commit=False)
            formInstance.author = request.user
            formInstance.save()
            return redirect("home")

    form = forms.CreateNewArticle
    return render(request, 'articles/createArticle.html', {"form": form})


def DetailArticle(request, slug):
    article = models.Article.objects.get(slug=slug)
    return render(request, 'articles/detail.html', {"article":article})


def ArticleList(request):
    articles = models.Article.objects.all().order_by('-date')
    return render(request, 'articles/list.html', {"articles":articles})