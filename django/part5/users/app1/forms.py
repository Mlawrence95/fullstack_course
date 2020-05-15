from django import forms
from django.contrib.auth.models import User
from app1.models import UserProfileInfo

class UserProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model  = User
        fields = ["username", "email", "password"]


class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model  = UserProfileInfo
        fields = ['portfolio', 'picture']
