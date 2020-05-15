from django.urls import path
from app1 import views

# TEMPLATE TAGGING
app_name = "app1"

urlpatterns = [
    path("registration", views.register, name='register'),
    path("", views.login, name="login")
]
