from datetime import datetime
from config import db, ma


class Movie(db.Model):
    __tablename__ = "movie"
    movie_id = db.Column(db.Integer, primary_key=True)
    popularity = db.Column(db.String(32))
    director = db.Column(db.String(32))
    genre = db.Column(db.String(32))
    imdb_score = db.Column(db.String(32))
    name = db.Column(db.String(32))


class MovieSchema(ma.ModelSchema):
    class Meta:
        model = Movie
        sqla_session = db.session
