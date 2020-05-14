from django import forms
from django.core import validators
from .models import User


class MyForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name  = forms.CharField()
    email      = forms.EmailField()
    email2     = forms.EmailField(label="Enter your email again:")

    def clean(self):
      all_clean_data = super().clean()
      email = all_clean_data['email']
      verif = all_clean_data['email2']

      if email != verif:
        raise forms.ValidationError("Make sure emails match!")

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
