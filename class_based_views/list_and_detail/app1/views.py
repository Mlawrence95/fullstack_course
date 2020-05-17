from django.views.generic import (TemplateView, ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from app1.models import School, Student

class CBView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["injectme"] = "Hello, welcome to the index page."
        return context


class SchoolListView(ListView):
    context_object_name = "school_list"
    model = School
    template_name = "app1/school_list.html"


class SchoolDetailView(DetailView):
    context_object_name = "school_detail"
    model = School
    template_name = "app1/school_detail.html"


class SchoolCreateView(CreateView):
    # allow users to add a school
    fields = ["name", "principal", "location"]
    model = School
    template_name_suffix = '_update_form'


class SchoolUpdateView(UpdateView):
    # allow users to update an entry for school in the db
    fields = ["name", "principal"]
    model = School
    # this looks for app1/<Model name>_update_form.html
    template_name_suffix = '_update_form'


class SchoolDeleteView(DeleteView):
    model = School
    # only evaluate when necessary
    success_url = reverse_lazy("app1:school_list")
    template_name_suffix = '_confirm_delete'
