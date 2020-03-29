from celery import Celery
from celery.schedules import crontab

from utils.db_updater import DatabaseUpdater


class Config:
    CELERY_RESULT_EXPIRES = 3600
    CELERY_ACCEPT_CONTENT = ['application/json']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'


app = Celery(
    'tasks',
    backend='redis://imdb_ratings_redis:6379/0',
    broker='redis://imdb_ratings_redis:6379/0',
)
app.config_from_object(Config)

app.conf.beat_schedule = {
    'backup_db': {
        'task': 'celery_init.update_db',
        'schedule': crontab(hour='*/24'),
    },
}


@app.task(bind=True)
def update_db(self):
    DatabaseUpdater().run()
