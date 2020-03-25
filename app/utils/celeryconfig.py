from celery.schedules import crontab


CELERY_IMPORTS = ('utils.tasks.update_database')
CELERY_TASK_RESULT_EXPIRES = 30
CELERY_TIMEZONE = 'UTC'

CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERYBEAT_SCHEDULE = {
    'test-celery': {
        'task': 'utils.tasks.update_database',
        'schedule': crontab(days="7"),
    }
}