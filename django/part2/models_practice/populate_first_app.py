# populate.py
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "boilerplate_django.settings")

import django
django.setup()

### Fake population
import random
from app1.models import Topic, Webpage, AccessRecord
from faker import Faker

fakegen = Faker()
topics  = ["Search", "Social", "Marketplace", "News", "Games"]

def add_topic():
    # retrieve topic if it exists, or create
    # [0] is a reference to the model instance
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        # get topic for entry
        top = add_topic()

        # create the fake data for entry
        fake_url  = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # create Webpage()
        webdata = {
            "topic": top,
            "url": fake_url,
            "name": fake_name
        }
        web = Webpage.objects.get_or_create(**webdata)[0]

        # create AccessRecord()
        accessdata = {
            "name": web,
            "date": fake_date
        }
        record = AccessRecord.objects.get_or_create(**accessdata)[0]

if __name__ == "__main__":
    print("populating database with fake data!")
    populate(20)
    print("population complete!")
