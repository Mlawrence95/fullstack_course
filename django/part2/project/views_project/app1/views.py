from django.shortcuts import render
from app1.models import User

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
