from __future__ import absolute_import
from celery import Celery

from celery.schedules import crontab
from celery.decorators import periodic_task
import requests
import json
import time

app = Celery('tasks', broker='redis://localhost')

@periodic_task(
    run_every=(crontab(minute='*/1')),
    name="create_session",
    ignore_result=True
)
def create_session():
    r=requests.post('http://localhost:8000/sessions/', data={'num_votes':0})
    data =r.json()
    session_id = data['id']
    time.sleep(3)
    r=requests.put('http://localhost:8000/sessions/'+str(session_id)+'/', data={'num_votes':1})
    return r.json()

if __name__ == "__main__":
    app.start()
