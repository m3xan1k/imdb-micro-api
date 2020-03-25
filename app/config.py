import os


DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///data/test.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True

# redis, celery
REDIS_HOST = "0.0.0.0"
REDIS_PORT = 6379
BROKER_URL = os.environ.get(
    'REDIS_URL', "redis://{host}:{port}/0".format(host=REDIS_HOST, port=str(REDIS_PORT)))
CELERY_RESULT_BACKEND = BROKER_URL
