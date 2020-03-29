import unittest
import urllib.request
import os

from app import app, db
from app.models import Rating


class RatingTest(unittest.TestCase):

    API_URL = os.environ.get('VIRTUAL_HOST')

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_rating(self):
        movie_rating = Rating(
            imdb_id='asdf123',
            rating=5.0,
            votes=1000,
        )
        db.session.add(movie_rating)
        db.session.commit()

        response_1 = urllib.request.urlopen(f'http://{self.API_URL}')
        assert response_1.status == 400

        response_2 = urllib.request.urlopen(f'http://{self.API_URL}/?imdb_id=zcxv321')
        assert response_2.status == 404

        response_3 = urllib.request.urlopen(f'http://{self.API_URL}/?imdb_id=asdf123')
        assert response_3.status == 200
