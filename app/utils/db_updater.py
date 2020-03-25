import csv
import urllib.request
import gzip
import io

from tqdm import tqdm

from app.api import MovieRating
from app.api import db


class DatabaseUpdater:

    RATINGS_DATASET_URL = 'https://datasets.imdbws.com/title.ratings.tsv.gz'

    @classmethod
    def fetch_data(cls) -> str:
        # get zipped archive from imdb
        response = urllib.request.urlopen(cls.RATINGS_DATASET_URL)
        if not response.code == 200:
            raise ValueError(f'IMDB server responsed with status {response.code}')
        zipped_bytes = io.BytesIO(response.read())

        # unzip and return string
        with gzip.GzipFile(fileobj=zipped_bytes, mode='rb') as f:
            csv_content = f.read()
        return csv_content.decode('utf-8')

    @staticmethod
    def fill_database(csv_content: str) -> None:
        # load csv content to csv.reader
        csv_file_obj = io.StringIO(csv_content)
        reader = csv.reader(csv_file_obj, delimiter='\t')

        # make 'cache' from all imdb_ids in local db
        imdb_ids_query = db.session.query(MovieRating.imdb_id)
        local_imdb_ids = set([_id for _id, in imdb_ids_query.all()])

        # skip csv header
        next(reader)
        movie_ratings = []
        for row in tqdm(reader):
            # check suck imdb_id already in local db
            if row[0] in local_imdb_ids:
                continue

            # init object, collect them and fill db
            movie_rating = MovieRating(
                imdb_id=row[0],
                rating=float(row[1]),
                votes=int(row[2]),
            )
            movie_ratings.append(movie_rating)
        if movie_ratings:
            print(f'loading to db {len(movie_ratings)}')
            db.session.bulk_save_objects(movie_ratings)
            db.session.commit()

    def run(self) -> None:
        csv_content = self.fetch_data()
        self.fill_database(csv_content)
