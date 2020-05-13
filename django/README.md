# Django Notes

## Install `django_env`
Do this by using `conda env create -f environment.yml`

## Create a project
Use `django-admin startproject <proj name>` to build out the skeleton of a project.

## Skeleton Files

### settings.py
This contains all of the project settings.

### urls.py
Contains all of the URLs necessary to show the different pages for your site. Can be REGEX heavy.

### wsgi.py
Web Server Gateway Interface. This file is useful for deploying your app.

### manage.py
Handles a lot of important commands for handling your web app. For example,
```bash
$ python manage.py runserver
```

is the code needed to start your server.

## Migrations
A way to move a database from one design to another (perhaps adding more column).

## Django Applications
A Django application is not necessarily the full website. The phrase Django application typically refers to a module that may be combined with other modules to make a full site. An example of this may be a set of views and their backend that handle checking your account balance on a bank's website.

Create an app skeleton with this command:
```bash
$ python manage.py startapp <app name>
$ ls <app name>
__init__.py	apps.py	models.py	views.py
admin.py	migrations	tests.py
```
### Adding the app to our project
Each app must be registered in `project/settings.py` in the `INSTALLED_APPS` field, simply using the name of the app. This looks like:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "apptwo"
]
```

To route correctly, the app must then be registered in `project/urls.py` like so:
```python
from django.contrib import admin
from django.urls import path
from first_app.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index")
]
```

where the first param in `path` gives the endpoint to access the view. Here we have `http://127.0.0.1:8000/admin` and `http://127.0.0.1:8000/`, respectively.

### admin.py
This allows you to register your models with Django, unlocking some features in the admin interface.

### app.py
Handles app-specific configuration.

### models.py
Store the application's data models (the relationships between each entity).

### tests.py
Unit tests and the like.

### views.py
Handle requests and their responses. For example,

```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World!")
```

### app/migrations/ folder
Database-specific information as it relates to the models.


## Modular URL mapping
We can add a `urls.py` folder to each `app` structure instead of the main project, linking each app into the project with an `include()` call. This makes the URL mappings modular and thus scalable.

Example: Consider a project with the following structure

- proj
  - urls.py
  - ...
- module
  - urls.py
  - ...

To route urls from the app `module` to the main project, `proj`, we need to modify each of the `urls.py` files.

`proj.urls`:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("apptwo.urls"), name="index")
]
```

`module.urls`
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

For reminders, check out the [documentation](https://docs.djangoproject.com/en/3.0/intro/tutorial01/).


## Templates

Templates are a way to contain the parts of a view that are static, allowing each page to inherit a base, foundational view. By convention, each django app should have its own folder in the project. The structure is this:

- web/
  - manage.py
  - app1/
  - app2/
  - project/
    - ...
  - templates/
    - app1/
      - app1.html
    - app2/
      - app2.html
    - ...



Django must be made aware of the templates by editing the `DIRS` field in the `TEMPLATES` variable of `project/settings.py`. For flexibility, this variable should be set dynamically using `os`. Given the `BASE_DIR` variable in `settings.py`, the correct path for `/templates/` can be calculated like:

```python
TEMPLATES_PATH = os.path.join(BASE_DIR, "templates")
```

### Template tags
These are a way to inject information from your backend into the browser. Here's one such example:

```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>First app</title>
  </head>
  <body>
    <h1>This is index.html</h1>
    {{ insert_me }}
  </body>
</html>

```

The `insert_me` field here is something that can be passed along at render time.
That process looks like the following:

```python
# This is views.py for my app
from django.shortcuts import render

# Create your views here.
def index(request):
    my_fields = {
        "insert_me": "hello I am from views.py"
    }
    return render(request, "app1/index.html", context=my_fields)
```


## Static files
For a Django project to be aware of static files, we must alter `settings.py` to have
a global that dynamically points to our media location. Consider a simple case, where we want
to keep some images around for our project. We should make a file structure like the following:

- project/
  - urls.py
  - settings.py
  - ...
- manage.py
- app1/
- templates/
- static/
  - img.png
  - img2.png
  - ...

For this `static/` folder to be useful, we must add reference to it in our `settings.py`.
Do this by adding the following:
```python
# settings.py
STATIC_DIR = os.path.join(BASE_DIR, "static")
```

and then additional structure must be added (the name is important!).

Note: there is a `static_url` section at the bottom of `settings.py` already.
This is the url that static content will be accessible from on the server. It can
be protected if you so choose.

```python
# settings.py
STATICFILES_DIRS  = [
    STATIC_DIR,
]
```
With this in place, you should now be able to see `img.png` at `127.0.0.1:8000/static/img.png`.
Realistically, we'd like to use the images in our HTML files. Injecting an image into
HMTL is not so different from injecting text, as we've done before.

Here's an example of how we can inject in image into our HTML file given the following directory structure:
- manage.py
- project/
  - urls.py
  - settings.py
  - ...
- app1/
- templates/
- static/
  - app1/
    - css/
    - js/
    - img.png
  - ...

```html
<!DOCTYPE html>
{% load static %}
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>ML Art</title>
  </head>
  <body>
    <h1>Here is some ML-generated art!</h1>

    <img src="{% static 'app1/img.png' %}"
    alt="There was a problem loading our content. :(">

  </body>
</html>
```

Static files don't have to be images. We can keep other useful files in static as well,
such as our `.js` and `.css` files. Linking CSS and Javascript is simple -- notice the small
modification we can make to include a CSS file from our static directory:
```HTML
<!DOCTYPE html>
{% load static %}
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>ML Art</title>

    <link rel="stylesheet" href="{% static 'picServer/css/app.css' %}">

  </head>
  <body>
    <h1>Here is some ML-generated art!</h1>

    <img src="{% static 'picServer/picasso.png' %}"
    alt="There was a problem loading our content. :(">

  </body>
</html>
```
