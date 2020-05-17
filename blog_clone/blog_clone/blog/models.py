from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class BlogPost(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title  = models.CharField(max_length=200)
    blog_content = models.TextField()
    create_date  = models.DateTimeField(timezone.now())
    publish_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(is_approved=True)

    def get_absolute_url(self):
        # go to blog post when created
        return reverse("post_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title


class BlogComment(models.Model):
    parent_post = models.ForeignKey(BlogPost,
                                    related_name="comments",
                                    on_delete=models.CASCADE)
    author  = models.CharField(max_length=100)
    content = models.TextField()

    create_date = models.DateTimeField(timezone.now())
    is_approved = models.BooleanField(default=False)

    def approve(self):
        self.is_approved = True
        self.save()

    def get_absolute_url(self):
        # when comment is submitted, go back to blog post
        return self.post.get_absolute_url()
