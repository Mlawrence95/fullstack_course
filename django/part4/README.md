# Django URLs, Templates, and more!
## (...The main README file is pretty bloated right now)

### Relative URLs
URLs and their routing have been touched on in previous lessons, but here's a refresher.
Each project comes with its own `urls.py` files that determines which `views` to
show for each branch from the root directory of your site. It looks like this:

```python
# project/urls.py
from django.contrib import admin
from django.urls import path, include
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("basic_app/", include("app1.urls")) # the / is important
]
```
The first path is the built-in admin page. The second is the home page one reaches
when first entering the site, and is linked to `app1`'s `views.py` file to render
index. The third part is allowing branching. This syntax says that, should someone
go to `http://127.0.0.1:8000/basic_app/*`, whichever page they go to at that branch
should be matched against `app1/urls.py`.

```python
# app1/urls.py
from django.urls import path
from app1 import views

# TEMPLATE TAGGING
app_name = "app1"

urlpatterns = [
    path('relative', views.rel_url, name='relative'),
    path("other", views.other, name="other")
]
```

This means that we have 4 routes set up:
- admin: `http://127.0.0.1:8000/admin/`
- home: `http://127.0.0.1:8000/`
- relative: `http://127.0.0.1:8000/basic_app/relative/`
- other: `http://127.0.0.1:8000/basic_app/other`

Since we set `app_name` in `app1/urls.py`, we can use template tagging to
link HTML pages together like so:

```HTML
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <h1>Welcome to relative urls!</h1>
    <h3>Here is the <a href="{% url 'app1:other' %}">other</a> page.</h3>
  </body>
</html>
```

Notice the `href` calling `<app_name>:<view name>` to create a relative link. Nice!
The same pattern can be used to link to the admin page and other built-in Django
pages.

1. Admin index page (may need to run `migrate`):
  - `<a href="{% url 'admin:index' %}">admin home page</a>`
2. Our project index page:
  - `<a href="{% url 'index' %}">Home Page!</a>`


### Template Inheritance (Template extending)
Create a base page or pages, then add on only what you need for each view.

This is the base file, `basic_app/base.html`.
```
<links to JS, CSS, BOOTSTRAP, etc>
<Basic style, such as navbars>
  <body>
  {% block body_block %}
  {% endblock %}
  </body>
</footer html>
```

Each subsequent HTML file then extends the correct base files.
```
<!DOCTYPE html>
{% extends "basic_app/base.html" %}
{% block body_block %}
  <html specific to this file>
  <html specific to this file>
  <html specific to this file>
{% endblock %}
```

Note that you can have different blocks. We named ours `body_block`, but
the block can take on any name for your purposes.


### Template Filters
Template filters are a way to interact with data as it is injected into your page
via a template tag. These look like, `{{ value | filter: "parameter"}}`, though not all filters will have a parameter. There are built-in filters, as well as ways to create a custom filter. Documentation on template filters and other HTML
html inject logic is [here](https://docs.djangoproject.com/en/3.0/ref/templates/builtins/#built-in-template-tags-and-filters).

example:
```html
{{ django |title }}
{{ number | add:"5" }}

```
This would look for the injected key called `django`, and apply `.title()` to its
value (it better be a string). `number` would simply have 5 added to it.

#### Custom template
First, for a directory like,

```
- project/
  - settings.py
- app1/
  - views.py
manage.py
```

add a new `templatetags` folder to `app1`, along with `__init__.py` and a source file, like:
```
- project/
  - settings.py
- app1/
  - views.py
  - templatetags/
    - __init__.py
    - my_extras.py
manage.py
```

Then, to register a new filter, do the following in `my_extras.py`:

```python
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@stringfilter
def combine_arg(value, arg):
    return f"{value} {arg}"

register.filter("combarg", combine_arg)
```


Now, if a HTML file contains `{% load my_extras %}`, this filter will be available. Note that simply having this load in a base html file doesn't work...
Not sure why.
