from time import sleep
from celery import shared_task
from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json

@shared_task
def tes(id):
    print('session storage cleared')
    print(id)
    return id

@shared_task
def clear():
    print('clearing cashe')
    return 999

# CODE FOR CREATING INTERVAL SHEDULER

schedule, created = IntervalSchedule.objects.get_or_create(
    every = 15,
    period = IntervalSchedule.SECONDS
)


# CODE FOR SCHEDULE THE PERIODIC TASK
PeriodicTask.objects.get_or_create(
    name = 'clear cookies',
    task = 'app.tasks.clear',
    interval = schedule,
    args =  json.dumps([])
)