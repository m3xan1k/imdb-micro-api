from flask import Flask, request, make_response
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from app.models import MovieRating
from app.serializers import MovieRatingSchema
from app.views import RatingView


app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
ma = Marshmallow(app)


app.add_url_rule('/rating/', view_func=RatingView.as_view('rating'))


if __name__ == '__main__':
    app.run('0.0.0.0', port=8000, debug=True)
