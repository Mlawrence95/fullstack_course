from django.shortcuts import render

# Create your views here.
def index(request):
    data = {
        "info": "Hello world"
    }
    return render(request, "app1/index.html", context=data)
