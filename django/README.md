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


## Models and Databases

Django comes equipped with `sqlite`, though any engine can be swapped in via
the `ENGINE` param in `settings.py`.

To create a `model`, we use a class structure
inside of each application's `models.py` file (documentation [here](https://docs.djangoproject.com/en/3.0/topics/db/models/)). Each object will subclass
`django.db.models.Model`, while each attribute of the class represents a field,
having the same constraints as a column in SQL. Each column has a type,
such as `CharField`, `IntegerField`, `DateField`, and so on. Each field can also
have constraints. For example, `CharField` should have a `max_length` constraint.

There is also a notion of relationships between fields, which we describe using
primary keys and foreign keys. A `primary key` is a unique identifier for each row in a
table. A `foreign key` is a value that, for an observation/datapoint/row in a database,
 maps to a primary key of another table.

example class structure:
```python
# app/models.py
class Topic(models.Model):
  top_name = models.CharField(max_length=264, unique=True)

class Webpage(models.Model):
  # on_delete says to delete the data in this table if the parent row is deleted
  category = models.ForeignKey(Topic, on_delete=models.CASCADE)
  name     = models.CharField(max_length=264)
  url      = models.URLField()
```

Each of these classes will act like a table in the database, which Django will set up for you.
To enact this change, run `python manage.py migrate`. Register the changes to your
app like, `python manage.py makemigrations <app name>`. After `makemigrations`
is ran on your apps, rerun `python manage.py migrate`. In order to use the admin interface
with the models, each model must be registered in `admin.py` like follows:

```python
# admin.py
from django.contrib import admin
from app.models import Topic, Webpage

admin.site.register(Topic)
admin.site.register(Webpage)
```

In order to use the database as and Admin, we need to create a `superuser`. This
can be created using `python manage.py createsuperuser`. You will need a name, email,
and password. To test databases and models, it's a good idea to populate them with fake data
(we can use a library called Faker and create a script for this).

### Interacting with your Models
Having ran the migrations for your database, you can verify that the models are
set up correctly by using `python manage.py shell`. From this shell, for the above models:
```python
>>> from app1.models import Topic
>>> print(Topic.objects.all())
<QuerySet []> # There are no Topic objects in the db yet
>>> t = Topic(top_name="Social Network")
>>> t.save()
>>> print(Topic.objects.all())
<QuerySet [<Topic: Social Network>]> # we've added an entry to the db
```

It's more practical, however, to use the admin panel. As mentioned before, this can
be done by creating a `super user`. Note: there is currently a bug where, upon accessing
the admin panel, the Django server dies. This can be resolved by using python 3.8
(thus the versioning in `environment.yml`).

If you access the dashboard successfully, you should see the database fields provided.
![admin dash](media/adminDash.png)


### Populating Models with Fake Data

The `faker` library implements and easy-to-use library for generating fake data.
We can create a population script to stub the database in a very simple way.
Note that the values passed for foreign keys must be actual *instances* of the
referenced object, not a simple data type.

```python
# populate.py
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "boilerplate_django.settings")

import django
django.setup()

### Fake population
import random
from app1.models import Topic, Webpage, AccessRecord
from faker import Faker

fakegen = Faker()
topics  = ["Search", "Social", "Marketplace", "News", "Games"]

def add_topic():
    # retrieve topic if it exists, or create
    # [0] is a reference to the model instance
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        # get topic for entry
        top = add_topic()

        # create the fake data for entry
        fake_url  = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # create Webpage()
        webdata = {
            "topic": top,
            "url": fake_url,
            "name": fake_name
        }
        web = Webpage.objects.get_or_create(**webdata)[0] # <-- [0]!!

        # create AccessRecord()
        accessdata = {
            "name": web,
            "date": fake_date
        }
        record = AccessRecord.objects.get_or_create(**accessdata)[0] # <-- [0]!!

if __name__ == "__main__":
    print("populating database with fake data!")
    populate(20)
    print("population complete!")

```


## MTV - Models, Templates Views

A paradigm of connecting everything together in your stack.

1. Use `views.py` to import any `model` we need.
2. Query the `model` for any data that we need
3. Pass results from the model query to a template
4. Edit the template to accept and display data from the model (tagging)
5. Map a URL to the view

To inject information from our tables into a view, we only have to slightly change
our existing method of using `render` to utilize the queried data. Here's an
example:
```python
# views.py
from django.shortcuts import render
from app1.models import Topic, Webpage, AccessRecord

# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by("date")

    date_dict = {
        "access_records": webpages_list
    }

    return render(request, "app1/index.html", context=date_dict)
```

The `html` injection needed to support this is a little more complex than we're
used to. Here's one way we can consume the data in our page:

```HTML
<!DOCTYPE html>
{% load static %}
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Hello World</title>

    <link rel="stylesheet" href='{% static "app1/css/index.css" %}'>
  </head>
  <body>
    <h1>Hello there!</h1>
    <h2>Here are the access records.</h2>

    <div class="djangTwo">
      {% if access_records %}
        <table>
          <thead>
            <th>Site Name</th>
            <th>Date Accessed</th>
          </thead>
        {% for acc in access_records %}
        <tr>
          <td>{{acc.name}}</td>
          <td>{{acc.date}}</td>
        </tr>
        {% endfor %}

      </table>
      {% else %}
        <p>No records found</p>
      {% endif %}

    </div>

  </body>
</html>
```

The results of this injection with our stubbed database look great!


![View of our database information](media/tableView.png)

## Forms, Requests, and Data Validation

Forms in Django allow easily getting data from the
frontend into python data structures in the backend. A Django form works very similar to a `model`. To
start, we must create a `/app/forms.py` file. Inside this `forms.py`, you must have something like this:
```python
from django import forms

class FormName(forms.Form):
  name  = forms.CharField()
  email = forms.EmailField()
  text  = forms.CharField(widget=forms.Textarea)
```

The form must then be injected via your `views.py` file, like so:

```python
from forms import FormName

def form_name_view(request):
  form = FormName()
  data = {
    "form": form,
    "other_injectable": None
  }
  return render(request, "form_name.html", context=data)
```

Of course, having a new view, we must specify the new URL either directly or with `include()`, such as:

```python
from app import views

urlpatterns = [
  path("formpage/", views.form_name_view, name="form_name")
]
```

From here, the HTML page can simply render the form using a template tag like `{{ form }}`; however, forms rendered this way will be fairly plain, and they won't have the typical HTML tags to make styling easy. More realistically, we can wrap the form injection with some HTML like this:

```html
<div class="container">
  <form method="post">
    {{ form.as_p }}
    {% csrf_token %}
    <input type="submit" class="btn btn-primary" value="Submit">
  </form>
</div>
```

By using `as_p`, each form element will be wrapped with `<p>` tags, making them look a little prettier. Additionally, the `csrf_token` is *REQUIRED* by Django, and finds an easy way to be inserted with this method. CSRF is Cross-Site Request Forgery, and its token makes sure that the HTTP POST action is performed with integrity.

This example would actually do nothing upon pressing `submit` as it currently stands. For a submission to be handled, the `views.py` view  must have explicit handling of the `POST` request. Luckily, Django gracefully handles forms, cleaning the data and validating its inputs, making them easy to access. A better view would be this:

```python
# views.py
from forms import FormName

def form_name_view(request):
  form = FormName()

  if request.method == "POST":
    # override the original form with this POST version
    form = FormName(request.POST)

    if form.is_valid():
      # Do stuff with the data
      print("form validation successful")
      print(f"Name is {form.cleaned_data['name']}")
      print(f"Email is {form.cleaned_data['email']}")
      print(f"Freeform text is {form.cleaned_data['text']}")

  data = {
    "form": form,
    "other_injectable": None
  }
  return render(request, "form_name.html", context=data)
```

### Requests

#### HTTP
Hypertext Transfer Protocol, designed to enable communication between a client and a server. The client submits a request, and the server responds.

#### GET
Requests data from a resource.

#### POST
Submits data to be processed.

### Form Validation

#### Hidden fields
One way to catch bad input for a form is to have a hidden field that solicits input,
catching bots that automatically fill out all input fields they find. This is
straightforward to implement:

```python
# forms.py
from django import forms

class MyForm(forms.Form):
    name  = forms.CharField()
    email = forms.EmailField()
    text  = forms.CharField(widget=forms.Textarea)

    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput)


    def clean_botcatcher(self):
        bot = self.cleaned_data["botcatcher"]

        if len(bot) > 0:
            raise forms.ValidationError("GOTCHA BOT!")

        return bot
```

However, Django supplies form validators making the explicit check unnecessary. A more  
realistic validation check would rely on the built-in tools:

```python
from django import forms
from django.core import validators

class MyForm(forms.Form):
    name  = forms.CharField()
    email = forms.EmailField()
    text  = forms.CharField(widget=forms.Textarea)

    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])
```

#### Custom validation

Validators can be used for any fields. In fact, custom validators are easily
implementable as well. Imagine you'd like to force a field to start with the letter `z`.
You can implement a validator like:

```python
from django import forms
from django.core import validators

def check_for_z(value):
  if value[0].lower() != 'z':
    raise forms.ValidationError("NAME NEEDS TO START WITH Z!")


class MyForm(forms.Form):
    name  = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    text  = forms.CharField(widget=forms.Textarea)

    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])
```

Perhaps you want to do validation against multiple fields at once, such as during account
creation, where you'd want to ensure that the email was specified correctly. One
can invoke underlying Django methods to do this easily:

```python
from django import forms
from django.core import validators

class MyForm(forms.Form):
    name   = forms.CharField(validators=[check_for_z])
    email  = forms.EmailField()
    email2 = forms.EmailField(label="Enter your email again:")
    text   = forms.CharField(widget=forms.Textarea)

    def clean(self):
      all_clean_data = super().clean()
      email = all_clean_data['email']
      verif = all_clean_data['email2']

      if email != verif:
        raise forms.ValidationError("Make sure emails match!")
```


### Merging Forms with Models

Doing this requires some minor changes to how we've approached forms in the past.
For one, our `form` class will now need to inherit from `django.forms.ModelForm`.
Additionally, we need a `Meta` class embedded within our `form` class to connect
the form data to our model. This would look like:

```python
# forms.py
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
        model  = User
        fields = ["first_name", "last_name", "email"] # "__all__" is fine too
```

Adding this data to the database is then a simple extension of the code we've
built up for `views.py`:

```python
# views.py
from django.shortcuts import render
from app1.models import User
from app1.forms import MyForm


def form_view(request):
    form = MyForm()

    if request.method == "POST":
        form = MyForm(request.POST)

        if form.is_valid():
          # dump to database
          form.save(commit=True)
          print("form validation successful")

    data = {
        "form": form
    }
    return render(request, "app1/form_view.html", context=data)
```
