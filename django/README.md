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

- manage.py
- project
  - templates
    - app1
    - app2
    - ...
  - app1/
  - app2/
  - ...


Django must be made aware of the templates by editing the `DIRS` field in the `TEMPLATES` variable of `project/settings.py`. For flexibility, this variable should be set dynamically using `os`. Given the `BASE_DIR` variable in `settings.py`, the correct path for `/templates/` can be calculated like:

```python
TEMPLATES_PATH = os.path.join(BASE_DIR, "templates")
```
