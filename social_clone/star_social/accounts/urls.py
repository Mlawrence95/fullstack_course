from django.contrib import admin
from django.urls import path

from django.contrib.auth.views import LoginView, LogoutView
from accounts import views

app_name = "accounts"

urlpatterns = [
    path("signup", views.SignUp.as_view(), name="signup"),
    path("login", LoginView.as_view(template_name="accounts/login.html"), name="signin"),
    path("logout", LogoutView.as_view(), name="signout")
]
