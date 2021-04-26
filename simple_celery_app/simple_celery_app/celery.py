import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simple_celery_app.settings')

app = Celery('simple_celery_app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

from datetime import timedelta

app.conf.beat_schedule = {
    'run-every-ten-seconds': {
        'task': 'simple_task.tasks.new_task',
        'schedule': timedelta(seconds=10),
    },
    'run-all-tasks-at-the-same-time':{
        'task': 'simple_task.tasks.all_tasks',
        'schedule': timedelta(seconds=15),
    },
}