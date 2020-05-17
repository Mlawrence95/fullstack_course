from django import forms
from blog.models import BlogPost, BlogComment


class PostForm(forms.ModelForm):

    class Meta:
        model  = BlogPost
        fields = ["author", "title", "blog_content"]

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "textinputclass"
                }),
            "blog_content": forms.Textarea(attrs={
                "class": "editable medium-editor-textarea postcontent"
            }),
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model  = BlogComment
        fields = ["author", "content"]

        widgets = {
            "author": forms.TextInput(attrs={
                "class": "textinputclass"
                }),
            "content": forms.Textarea(attrs={
                "class": "editable medium-editor-textarea"
            }),
        }
