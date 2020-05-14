# populate.py
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "boilerplate_django.settings")

import django
django.setup()

### Fake population
import random
from app1.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        # create the fake data for entry
        fake_first  = fakegen.first_name()
        fake_last   = fakegen.last_name()
        fake_email  = fakegen.ascii_email()

        # create Webpage()
        userdata = {
            "first_name": fake_first,
            "last_name":  fake_last,
            "email":      fake_email
        }
        use = User.objects.get_or_create(**userdata)[0]


if __name__ == "__main__":
    print("populating database with fake data!")
    populate(20)
    print("population complete!")
