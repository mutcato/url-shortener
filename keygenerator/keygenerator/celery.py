import os

from celery import Celery
from django.conf import settings


# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "keygenerator.settings")

app = Celery("keygenerator")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# A task that blocks indefinitely may eventually
# stop the worker instance from doing any other work.

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = settings.CELERYBEAT_SCHEDULE


@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))
