import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

app = Celery('app', broker='redis://localhost:6379')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
