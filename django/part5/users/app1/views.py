from django.shortcuts import render
from app1.forms import UserProfileForm, UserProfileInfoForm

# Create your views here.
def index(request):
    data = {
        "info": "Hello world"
    }
    return render(request, "app1/index.html", context=data)

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserProfileForm(request.POST)
        prof_form = UserProfileInfoForm(request.POST)

        if user_form.is_valid() and prof_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            # profile has 1:1 with user. tag the user
            profile = prof_form.save(commit=False)
            profile.user = user

            if "picture" in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True
        else:
            # forms aren't valid
            print(user_form.errors, prof_form.errors)
    else:
        # No POST -- render base form
        user_form = UserProfileForm()
        prof_form = UserProfileInfoForm()

    data = {
        'registered': registered,
        'user_form': user_form,
        'profile_form': prof_form
    }

    return render(request, "app1/registration.html", context=data)

def login(request):
    return render(request, "app1/login.html")
