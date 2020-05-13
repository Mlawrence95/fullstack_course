from django.shortcuts import render

# Create your views here.
def index(request):
    data = {
        "img_path": None
    }
    return render(request, "picServer/index.html", context=data)
