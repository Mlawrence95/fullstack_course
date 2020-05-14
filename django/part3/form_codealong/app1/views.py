from django.shortcuts import render
from .forms import MyForm

# Create your views here.
def index(request):
    data = {
        "info": "Hello world"
    }
    return render(request, "app1/index.html", context=data)

def form_view(request):
  form = MyForm()

  if request.method == "POST":
    # override the original form with this POST version
    form = MyForm(request.POST)

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
    return render(request, "app1/form_page.html", context=data)
