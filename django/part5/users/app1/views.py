from django.shortcuts import render
from app1.forms import UserProfileForm, UserProfileInfoForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    data = {
        "info": "Hello world"
    }
    return render(request, "app1/index.html", context=data)


@login_required
def special(request):
    return HttpResponse("You are logged in. Nice!")


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
        'registered':   registered,
        'user_form':    user_form,
        'profile_form': prof_form
    }

    return render(request, "app1/registration.html", context=data)


def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                print("logging in...")
                return HttpResponseRedirect(reverse("index"))
            else:
                return HttpResponse("Account Not Active")
        else:
            print("Someone tried to log in and failed.")
            return HttpResponse("invalid login details supplied")
    else:
        return render(request, "app1/login.html", context={})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
