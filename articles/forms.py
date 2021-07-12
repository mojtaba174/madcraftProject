from django import forms
from . import models


class CreateNewArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ["title", "slug", "body", "thumbnail", "description"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comments
        fields = ('name', "email", "body")
