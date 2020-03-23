import csv

from tqdm import tqdm

from api.app import MovieRating
from api.app import db


def fill_ratings():
    with open('./api/data/title.ratings.tsv') as f:
        reader = csv.reader(f, delimiter='\t')
        movie_ratings = []

        next(reader)
        for row in tqdm(reader):
            movie_rating = MovieRating(
                imdb_id=row[0],
                rating=float(row[1]),
                votes=int(row[2]),
            )
            movie_ratings.append(movie_rating)
    db.session.bulk_save_objects(movie_ratings)
    db.session.commit()
