# Handling Users -- Passwords, Authentication, Safety, and more

Much of what we're going to do depends on built-in Django functionality.
`project/settings.py` should contain `django.contrib.auth` and `django.contrib.contenttypes`, for starters.


## Password Security Basics

### NEVER STORE PASSWORDS AS PLAIN TEXT

We will begin with the PBKDF2 (SHA256) that is built-in, but we can easily add
even more security layers by pulling in `bcrypt` or `argon2`. Read more about
these security strategies for Django [here](https://docs.djangoproject.com/en/3.0/topics/auth/passwords/#using-argon2-with-django). We download these in `environment.yml` to make options available.

Additionally, password fields for models and forms can have validation applied
to them that allows for preventing weak password (no "password123" kind of stuff).

#### Using add-on hashers
To use an external password hasher, `settings.py` must be modified to be made
aware of the new hasher. Luckily, it's fairly simple
to do. Above `AUTH_PASSWORD_VALIDATORS`, we will do the following:

```python
# project/settings.py
PASSWORD_HASHERS = [
  'django.contrib.auth.hashers.Argon2PasswordHasher',
  'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
  'django.contrib.auth.hashers.BCryptPasswordHasher',
  'django.contrib.auth.hashers.PBKDF2PasswordHasher',
  'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher'
]
```
This provides a set of options for Django to handle the security of passwords. Additionally, you can find the current supported validators below, in a block like this:

```python
# project/settings.py
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
```
Notice that the name field for each of these is some constraint on password security. As Jose notes, striking the balance between security and user-friendliness is an important task when deciding how to use password validators. Let's explore how we'd customize the use of one of these validators:

```python
# project/settings.py
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        "OPTIONS": {
          'min_length': 9
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
```

Here we customized the minimum password length by changing the default value in
`OPTIONS` to something more strict. Nice and easy! Further documentation is
[here](https://docs.djangoproject.com/en/3.0/topics/auth/passwords/#module-django.contrib.auth.password_validation).


## Handling user-contributed media
If a user submits some information such as a profile picture, we currently don't
have a place to keep it. To handle this, we'll set up `media` at the project root,
just like `templates`.

The most basic config here should look like,
```python
# project/settings.py
MEDIA_DIR = os.path.join(BASE_DIR, "media")

# MEDIA
MEDIA_ROOT = MEDIA_DIR
MEDIA_URL  = "/media/"
```

## Creating a User profile

First, an important note: there already exists a built in `User` that we
should build our users in relation to; however, we should not subclass this user.
The base user has a few keys field, including:
- username
- email
- password
- first name
- last name
- is_active
- is_staff
- is_superuser

Extending the built-in `User` can be done by creating a new model that has a
one-to-one relationship with the base `User`. Here's an example:

```python
# models.py
from django.contrib.auth.models import User

# create your model that extends User here
class UserProfileInfo(models.Model):
  # create relationship to base User (do NOT inherit!)
  user = models.OneToOneField(User, on_delete=models.CASCADE)

  # tack on additional attributes
  portfolio = models.URLField(blank=True)
  picture   = models.ImageField(upload_to="profile_pics", blank=True)

  def __str__(self):
    # built-in attribute of django.contrib.auth.models.User
    return self.user.username
```

Don't forget to register this model in `admin.py` and migrate! We can then easily create a form that capture the additional attributes of our User. Additionally, having `upload_to` point to `profile_pics` implicitly assumes that there exists
`media/profile_pics/`. Get this set up.

```python
# forms.py
from django import forms
from app1.models import UserProfileInfo

class UserProfileInfoForm(forms.ModelForm):
  portfolio = forms.URLField(required=False)
  picture   = forms.ImageField(required=False)

  class Meta:
    model = UserProfileInfo
    exclude = ["user"]
```
