from django.urls import path
from app1 import views

# TEMPLATE TAGGING
app_name = "app1"

urlpatterns = [
    path("registration", views.register, name='register'),
    path("logged-in", views.user_login, name="login"),
    path("logged-out", views.user_logout, name="logout")
]
