from utils.celery_init import celery
from utils.db_updater import DatabaseUpdater


@celery.task()
def update_database():
    DatabaseUpdater().run()
