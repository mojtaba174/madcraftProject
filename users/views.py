from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm


def signup_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "users/sign_up.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect("home")

    form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')
    else:
        return redirect('home')


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')
    else:
        return redirect('home')


def dashboard_view(request):
    return render(request, 'users/dashboard.html')
