from django.urls import path
from app1 import views

app_name = "app1"

urlpatterns = [
    path('', views.CBView.as_view(), name='index'),
    path("school_list", views.SchoolListView.as_view(), name="school_list"),
    path("<int:pk>", views.SchoolDetailView.as_view(), name="school_detail"),
    path("create", views.SchoolCreateView.as_view(), name="create"),
    path("update/<int:pk>", views.SchoolUpdateView.as_view(), name="update"),
    path("delete/<int:pk>", views.SchoolDeleteView.as_view(), name="delete"),
]
