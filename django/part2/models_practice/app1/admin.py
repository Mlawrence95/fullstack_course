from django.contrib import admin
from app1.models import Topic, Webpage, AccessRecord

# Register your models here.
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
