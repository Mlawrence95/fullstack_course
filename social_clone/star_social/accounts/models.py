import django.contrib.auth.models as basemodels
from django.db import models

# Create your models here.
class User(basemodels.User, basemodels.PermissionsMixin):
# https://docs.djangoproject.com/en/3.0/ref/contrib/auth/
    def __str__(self):
        return f"@{self.username}"
