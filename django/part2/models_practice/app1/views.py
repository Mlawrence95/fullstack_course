from django.shortcuts import render
from app1.models import Topic, Webpage, AccessRecord

# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by("date")

    date_dict = {
        "access_records": webpages_list
    }

    return render(request, "app1/index.html", context=date_dict)
