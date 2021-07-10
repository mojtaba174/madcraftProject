from django.contrib import admin
from django.urls import path
from . import views

app_name = "articles"
urlpatterns = [
    path("create/", views.CreateArticle, name="create"),
    path("", views.ArticleList, name="list"),
    path('<slug>', views.DetailArticle, name="detail"),

]
