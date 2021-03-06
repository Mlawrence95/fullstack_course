from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import (TemplateView, ListView, UpdateView,
                                  DetailView, CreateView, DeleteView)

from blog.models import BlogPost, BlogComment
from blog.forms import PostForm, CommentForm

class AboutView(TemplateView):
    template_name = "blog/index.html"


class PostListView(ListView):
    """
    View: view list of published posts
    """
    model = BlogPost
    template_name = "blog/post_list.html"

    context_object_name = "post_list"

    def get_queryset(self):
        # get all blogposts less than or equal to (lte) current time
        # sort these with the nearest publish date first
        return (BlogPost.
                        objects.
                        filter(publish_date__lte=
                        timezone.now()).order_by("-publish_date")
                        )


class PostDetailView(DetailView):
    """
    View: views a single blog post
    """
    model = BlogPost
    template_name = "blog/blog_post.html"

    # retrieve HTML from here
    context_object_name = "post"


# should be logged in to access this. Use Auth Mixin
class CreateBlogPostView(CreateView, LoginRequiredMixin):
    """
    View: form for making a new blog post
    """
    # login mixin fields
    login_url           = "/login/"
    redirect_field_name = "blog:blog_post_view"

    # Create View fields
    model      = BlogPost
    form_class = PostForm
    template_name = "blog/create_post.html"


class UpdateBlogPostView(UpdateView, LoginRequiredMixin):
    """
    View: form for editing a blog post
    """
    # login mixin fields
    login_url           = "/login/"
    redirect_field_name = "blog:blog_post.html"

    # update View fields
    model      = BlogPost
    form_class = PostForm
    template_name = "blog/create_post.html"


class DeleteBlogPostView(DeleteView, LoginRequiredMixin):
    """
    View: prompt to delete a post
    """
    # delete View fields
    model = BlogPost
    success_url = reverse_lazy("blog:post_list")
    template_name = "blog/delete_post.html"


class DraftListView(ListView, LoginRequiredMixin):
    """
    View: view unpublished posts
    """
    # login mixin fields
    login_url           = "/login/"
    redirect_field_name = "blog:post_list"
    template_name       = "blog/post_draft_list.html"

    # drafts
    model = PostForm

    context_object_name = "draft_list"

    def get_queryset(self):
        return (BlogPost.
                    objects.
                    filter(publish_date__isnull=True).
                    order_by("create_date")
                    )


###############################################################################
# Begin functional views
###############################################################################

@login_required
def post_publish(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    blog_post.publish()
    return redirect("blog:blog_post_view", pk=pk)


def add_comment_to_post(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.parent_post = blog_post
            comment.save()
            return redirect("blog:blog_post_view", pk=blog_post.pk)
    else:
        form = CommentForm()
    return render(request, "blog/comment_form.html", context={"form": form})


@login_required
def approve_comment(request, pk):
    comment = get_object_or_404(BlogComment, pk=pk)
    comment.approve()
    return redirect("blog:blog_post_view", pk=comment.parent_post.pk)


@login_required
def remove_comment(request, pk):
    comment = get_object_or_404(BlogComment, pk=pk)
    # get pk of parent before deleting object
    blog_post_pk = comment.parent_post.pk
    comment.delete()
    return redirect("blog:blog_post_view", pk=blog_post_pk)
