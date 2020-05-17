# CBVs
Class based views and function based views are mostly interchangeable, though experienced users are more likely to use the
CBV. The two main places that change are `views.py` and `urls.py`.

Let's focus on a conversation case. With a function view, suppose we start with this `views.py` file:
```python
from django.shortcuts import render

def index(request):
  context = {"injectme": "hello"}
    return render(request, "app1/index.html")
```

The converted code for a CBV would look like:
```python
from django.views.generic import TemplateView

class CBView(TemplateView):
    template_name = "app1/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["injectme"] = "hello"
        return context
```

Then `urls.py` would have a path that looks like:
```python
...
from app1.views import CBView
urlpatterns = [
  path("", CBView.as_view()),
  ...
]
```

### Detail view and List view
The true power of CBV is in interacting with models and other complex data, such as looking at a single model entry or list of them. This approach should
handle patterns like `MyModel.objects.all()` with ease!

In this section, we will move templates to each app's folder, then explore the `ListView` and `DetailView` from `django.views.generic`

We'll make heavy use of the following models:

```python
from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # gets the URL of school detail for school having primary key pk
        return reverse("app1:school_detail", kwargs={"pk": self.pk})

class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School,
                               related_name="students",
                               on_delete=models.CASCADE)
    def __str__(self):
        return self.name
```

Consider the following `views.py` file for an app having models `School` and `Student`:

```python
from django.views.generic import ListView, DetailView
from app1.models import School, Student


class SchoolListView(ListView):
    context_object_name = "school_list"
    model = School
    template_name = "app1/school_list.html"


class SchoolDetailView(DetailView):
    context_object_name = "school_detail"
    model = School
    template_name = "app1/school_detail.html"
```

By setting our `context_object_name`, we can hook onto this attribute
in the respective HTML files to extract model information, like the following:

```HTML
<!DOCTYPE html>
{% extends "app1/app1_base.html" %}

{% block body_block %}
<ol>
  {% for school in school_list%}
  <h2>
    <li>
      <h2> <a href="{{school.get_absolute_url}}"> {{ school.name }} </a> </h2>
    </li>
  </h2>
  {% endfor %}
</ol>
{% endblock %}
```

Note that Django sets an `id` as the primary key for each `Student` and `School`.
Thus here we can link to a page built for each `School.id` -- this will be the
`school_detail.html` page for the school. This should look like:

```HTML
<!DOCTYPE html>
{% extends "app1/app1_base.html" %}

{% block body_block %}
<h1>Welcome to the School Detail Page</h1>
<h2>School details:</h2>
<p>Name: {{ school_detail.name }}</p>
<p>Principal: {{ school_detail.principal }}</p>
<p>Location: {{school_detail.location }}</p>

<h3>Students:</h3>

<!-- This accesses "related_name" from the Student Model to join the two objects -->
{% for student in school_detail.students.all %}
  <p>{{ student.name }} is {{student.age}} years old.</p>
{% end_for %}

{% endblock %}
```

To access this specialized html page for each primary key, `urls.py` must be
made aware that routing is being conditioned on a primary key, or `pk`. We
can handle this by making `urls.py` look like:

```python
from django.urls import path
from app1.views import CBView, SchoolListView, SchoolDetailView

app_name = "app1"

urlpatterns = [
    path('', CBView.as_view(), name='index'),
    path("school_list", SchoolListView.as_view(), name="school_list"),
    path("<int:pk>", SchoolDetailView.as_view(), name="school_detail"),
]
```

Notice that `school_detail` is now routing based on the primary key being passed
from our model. Ta da!


## CRUD - Create, Read, Update, Delete

CRUD is most naturally handled by CBV to provide the users of your site a way
to interact with the database in a non-technical way. We will use three new classes.

- `CreateView`
```python
# views.py
class SchoolCreateView(CreateView):
    fields = ["name", "principal", "location"]
    model = School
```

`models.py` must provide a way to look up the URL of a new
instance of the object, thus the use of [`get_absolute_url`](https://docs.djangoproject.com/en/3.0/ref/models/instances/#get-absolute-url).

```python
# models.py must have get_absolute_url
class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # gets the URL of school detail for school having primary key pk
        return reverse("app1:school_detail", kwargs={"pk": self.pk})
```
- `UpdateView`
- `DeleteView`
