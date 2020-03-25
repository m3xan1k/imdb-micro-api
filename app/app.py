from flask import Flask, request, make_response
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
ma = Marshmallow(app)


from imdb_ratings.views import *


if __name__ == '__main__':
    app.run('0.0.0.0', port=8000, debug=True)
