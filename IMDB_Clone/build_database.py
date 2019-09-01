import os
from config import db
from models import Movie

# Data to initialize database with
MOVIE = [
  {
    "popularity": 83.0,
    "director": "Victor Fleming",
    "genre": [
      "Adventure",
      " Family",
      " Fantasy",
      " Musical"
    ],
    "imdb_score": 8.3,
    "name": "The Wizard of Oz"
  },
  {
    "popularity": 88.0,
    "director": "George Lucas",
    "genre": [
      "Action",
      " Adventure",
      " Fantasy",
      " Sci-Fi"
    ],
    "imdb_score": 8.8,
    "name": "Star Wars"
  },
  {
    "popularity": 66.0,
    "director": "Giovanni Pastrone",
    "genre": [
      "Adventure",
      " Drama",
      " War"
    ],
    "imdb_score": 6.6,
    "name": "Cabiria"
  },
]


# Delete database file if it exists currently
if os.path.exists("movie.db"):
    os.remove("movie.db")

# Create the database
db.create_all()

# iterate over the MOVIE structure and populate the database
for movie in MOVIE:
    lgenre = movie.get("genre")
    lgenre = [x.strip() for x in lgenre]
    sorted(lgenre)
    str_genre = ', '.join(lgenre)
    m = Movie(popularity=movie.get("popularity"), director=movie.get("director"),genre=str_genre, imdb_score=movie.get("imdb_score"),name=movie.get("name"))
    db.session.add(m)

db.session.commit()
