import os

from celery import Celery


broker = 'redis://redis:6379/0'
backend = 'redis://redis:6379/0'

test_broker = 'redis://pvgl34353119a.apj.global.corp.sap:6379/0'
test_backend = 'redis://pvgl34353119a.apj.global.corp.sap:6379/0'

# set the default Django settings module for the 'celery' program.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'netease.settings')

# from django.conf import settings  # noqa

celery_app = Celery('netease', broker=test_broker, backend=test_backend, include=['async_tasks.tasks'])

celery_app.conf.update(
    result_expires=3600,
)

# Using a string here means the worker will not have to
# pickle the object when using Windows.
# celery_app.config_from_object('django.conf:settings')
# celery_app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


# if __name__ == "__main__":
#     celery_app.start()

from .tasks import taskA