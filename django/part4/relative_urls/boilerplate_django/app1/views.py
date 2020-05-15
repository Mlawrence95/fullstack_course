from django.shortcuts import render

# Create your views here.
def index(request):
    data = {
        "info": "Hello world",
        "number": 100
    }
    return render(request, "app1/index.html", context=data)

def other(request):
    return render(request, "app1/other.html")

def relative(request):
    return render(request, 'app1/rel_url.html')
