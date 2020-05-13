from django.shortcuts import render

# Create your views here.
def help(request):
    context = {
        "help_message": "Help Page"
    }
    return render(request, "helpPages/help.html", context=context)
