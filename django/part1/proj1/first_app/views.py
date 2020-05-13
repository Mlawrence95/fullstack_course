from django.shortcuts import render

# Create your views here.
def index(request):
    my_fields = {
        "insert_me": "hello I am from first_app/views.py"
    }
    return render(request, "first_app/index.html", context=my_fields)
