from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class ChangeEmail(forms.Form):
    email = forms.CharField(required=True, max_length=120, widget=forms.TextInput(attrs={'name': 'emailInput'}))


class ChangePassword(forms.Form):
    oldPassword = forms.CharField(required=True, min_length=8, max_length=80, widget=forms.PasswordInput(attrs={'name':"oldPassword"}))
    password1 = forms.CharField(required=True, min_length=8, max_length=80, widget=forms.PasswordInput(attrs={'name': 'password1'}), label="Password")
    password2 = forms.CharField(required=True, min_length=8, max_length=80, widget=forms.PasswordInput(attrs={'name': 'password2'}), label='Confirm password')
