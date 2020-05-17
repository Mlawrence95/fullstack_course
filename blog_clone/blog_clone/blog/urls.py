from django.urls import path, include
from blog import views

app_name = "blog"

urlpatterns = [
    path("about", views.AboutView.as_view(), name="about"),
    path("", views.PostListView.as_view(), name="post_list"),
    path("post/<int:pk>", views.PostDetailView.as_view(), name="blog_post"),
    path("post/new", views.CreateBlogPostView.as_view(), name="new_post"),
    path("post/<int:pk>/edit", views.UpdateBlogPostView.as_view(), name="edit_post"),
    path("post/<int:pk>/delete", views.DeleteBlogPostView.as_view(), name="delete_post"),
    path("drafts", views.DraftListView.as_view(), name="draft_list")
]
