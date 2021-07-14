from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, ChangeEmail, ChangePassword
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


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


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')
    else:
        return redirect('home')


@login_required(login_url='/users/login/')
def dashboard_view(request):
    return render(request, 'users/dashboard.html')


@login_required(login_url='/users/login/')
def UserDetail(request):

    user = request.user
    return render(request, "users/userDetail.html", {'user': user})


@login_required(login_url='/users/login/')
def ChangeEmail_view(request):
    user = User.objects.get(username=request.user.username)
    if request.method == "POST":
        changeEmailForm = ChangeEmail(request.POST)
        if changeEmailForm.is_valid():
            if user.email != changeEmailForm['email'].value():
                user.email = changeEmailForm['email'].value()
                user.save()
                return redirect('users:detail')
    changeEmailForm = ChangeEmail()
    return render(request, 'users/changeEmail.html', {'changeEmailForm':changeEmailForm})


@login_required(login_url="/users/login/")
def ChangePassword_view(request):
    user = User.objects.get(username=request.user.username)
    if request.method == "POST":
        passwordForm = ChangePassword(request.POST)
        if passwordForm.is_valid():
            if user.check_password(passwordForm['oldPassword']):
                if passwordForm['oldPassword'] != passwordForm['password1']:
                    if passwordForm['password1'].value() == passwordForm['password2'].value():
                        user.set_password(passwordForm['password1'].value())
                        user.save()
                        return redirect('users:detail')

    passwordForm = ChangePassword()
    return render(request, 'users/changePassword.html', {'passwordForm': passwordForm})


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
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})
