from flask.views import MethodView
from flask import request, make_response
from app import app

from imdb_ratings.models import MovieRating
from imdb_ratings.serializers import MovieRatingSchema


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
