from app import ma


class RatingSchema(ma.Schema):
    class Meta:
        fields = ('imdb_id', 'rating')
