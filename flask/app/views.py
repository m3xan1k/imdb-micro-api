from flask.views import MethodView
from flask import request, make_response
from app import app, db

from app.models import Rating
from app.serializers import RatingSchema


@app.errorhandler(404)
def not_found_error(error):
    return make_response({'msg': 'no such route'}, 404)


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return make_response({'msg': 'something went wrong'}, 500)


class RatingView(MethodView):
    methods = ['GET']
    rating_schema = RatingSchema()

    def get(self):
        imdb_id: str = request.args.get('imdb_id')
        if not imdb_id:
            return make_response({'error': 'imdb_id is required'}, 400)
        rating = Rating.query.filter_by(imdb_id=imdb_id).first()
        if not rating:
            return make_response({'msg': 'such imdb_id not found'}, 404)
        return self.rating_schema.dump(rating)


app.add_url_rule('/rating/', view_func=RatingView.as_view('rating'))
