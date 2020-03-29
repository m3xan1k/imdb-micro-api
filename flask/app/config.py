import os


PASS = os.environ.get('PGPASSWORD')
USER = os.environ.get('PGUSER')
DB = os.environ.get('PGDATABASE')
DEBUG = True
SQLALCHEMY_DATABASE_URI = f'postgresql://{USER}:{PASS}@imdb_ratings_db/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True
