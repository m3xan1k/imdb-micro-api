from flask import Flask, request, make_response
from flask.views import MethodView

from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
ma = Marshmallow(app)


class MovieRating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    imdb_id = db.Column(db.String(20), unique=True)
    rating = db.Column(db.Float)
    votes = db.Column(db.Integer, nullable=True)


class MovieRatingSchema(ma.Schema):
    class Meta:
        # model = MovieRating
        fields = ('imdb_id', 'rating')


class RatingView(MethodView):
    methods = ['GET']
    rating_schema = MovieRatingSchema()

    def get(self):
        imdb_id: str = request.args.get('imdb_id')
        if not imdb_id:
            return make_response({'error': 'imdb_id is required'}, 400)
        rating = MovieRating.query.filter_by(imdb_id=imdb_id).first()
        return self.rating_schema.dump(rating)


app.add_url_rule('/rating/', view_func=RatingView.as_view('rating'))


if __name__ == '__main__':
    app.run('0.0.0.0', port=8000, debug=True)
