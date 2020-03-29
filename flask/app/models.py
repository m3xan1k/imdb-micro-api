from app import db


class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    imdb_id = db.Column(db.String(20), unique=True)
    rating = db.Column(db.Float)
    votes = db.Column(db.Integer, nullable=True)
