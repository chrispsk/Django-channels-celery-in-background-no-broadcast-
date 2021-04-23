from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setari.settings')

app = Celery()

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'get-joke-every-3-seconds': {
        'task': 'get_the_joke',
        'schedule': 3.0
    }
}

app.autodiscover_tasks()
