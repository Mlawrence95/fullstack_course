from django.shortcuts import render
from app1.models import User
from app1.forms import MyForm

# Create your views here.
def user(request):
    # Sort by user first name LIMIT 10
    user_info = User.objects.order_by("first_name")[:10]
    data = {
        "user_info": user_info
    }
    return render(request, "app1/users.html", context=data)


def index(request):
    return render(request, "home/index.html")


def form_view(request):
    form = MyForm()

    if request.method == "POST":
        form = MyForm(request.POST)

        if form.is_valid():
          # Do stuff with the data
          form.save(commit=True)
          print("form validation successful")

    data = {
        "form": form
    }
    return render(request, "app1/form_view.html", context=data)
