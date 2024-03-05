import os
from celery import Celery
from time import sleep
from datetime import timedelta
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangocelery.settings')

app = Celery('djangocelery')


app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(name="test function")   #name for task but optional
def testing():
    print('testing start.......')
    sleep(3)
    print('testing end........')



@app.task
def check():

    print('this is check method.....')
    return 111



# TASK SHEDULER         #it can be write in settings.py

# app.conf.beat_schedule={
#     'after_10_second':{
#     'task':'app.tasks.tes',
#     'schedule':5,      # it take 5 seconds to schedule this task
#     # 'schedule': timedelta(seconds=4), # it deals with seconds only
#     'schedule':crontab(minute='*/1'),   # it deals with hour minuts and dat etc but not seconds
#     'args':('11',)
#     }
# }