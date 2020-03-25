from app.api import ma


class MovieRatingSchema(ma.Schema):
    class Meta:
        # model = MovieRating
        fields = ('imdb_id', 'rating')
