from flask import Flask, request, make_response
from flask.views import View


app = Flask(__name__)


class RatingView(View):
    methods = ['GET']

    def get(self):
        imdb_id: str = request.args.get('imdb_id')
        if not imdb_id:
            return make_response({'error': 'imdb_id is required'}, 400)


app.add_url_rule('/rating', view_func=RatingView.as_view('rating-view'))
