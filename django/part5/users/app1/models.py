from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
      # create relationship to base User (do NOT inherit!)
      user = models.OneToOneField(User, on_delete=models.CASCADE)

      # tack on additional attributes
      portfolio = models.URLField(blank=True)
      picture   = models.ImageField(upload_to="profile_pics", blank=True)

      def __str__(self):
        # built-in attribute of django.contrib.auth.models.User
        return self.user.username
