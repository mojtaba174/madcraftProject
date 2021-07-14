from django.contrib import admin
from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path("signup/", views.signup_view, name="signup"),
    path('logout/', views.logout_view, name="logout"),
    path('dashboard/', views.dashboard_view, name="dashboard"),
    path('dashboard/detail/', views.UserDetail, name="detail"),
    path('changeemail/', views.ChangeEmail_view, name="changeEmail"),
    path('changepassword/', views.ChangePassword_view, name="changePassword"),
    path("login/", views.login_view, name="login"),
]
