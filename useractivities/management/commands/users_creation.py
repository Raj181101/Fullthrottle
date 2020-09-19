from django.core.management.base import BaseCommand
from useractivities.models import User,ActivityPeriods
from datetime import datetime, timedelta
import random
from faker import Faker
from django.utils import timezone
#instance for the Faker object
fakedata = Faker()
from random import randint

class Command(BaseCommand):
    help = 'Fake Users Creation'

    ''' Run this command to create users (python manage.py users_creation 5 )'''

    def add_arguments(self, parser):
        parser.add_argument('no_of_users', type=int)

    def handle(self, *args, **kwargs):
        no_of_users = kwargs['no_of_users']
        for fakeuser in range(no_of_users):
          fake_id = fakedata.bothify(text='??#?##?##').upper()
          fake_name = fakedata.name()
          fake_tz = fakedata.timezone()
          fake_start_date = timezone.now() + timedelta(seconds=randint(0, 86400))
          fake_end_date = fake_start_date + timedelta(days=1)
          # Create new user Entry
          user = User.objects.create(id=fake_id,real_name=fake_name,tz=fake_tz)
          acty = ActivityPeriods.objects.create(user=user,start_time=fake_start_date,end_time=fake_end_date)
       
        return str(no_of_users)+' Users Created Succesfully'