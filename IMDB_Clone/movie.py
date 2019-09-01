"""
This is the movie module and supports all the ReST actions for the
MOVIE collection
"""

# System modules
from datetime import datetime

# 3rd party modules
from flask import make_response, abort


# Data to serve with our API
MOVIE = {
  "The Wizard of Oz":{
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
  "Star Wars":{
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
  "Cabiria":{
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
}


def read_all():
    """
    This function responds to a request for /api/movie
    with the complete lists of movie

    :return:        json string of list of movie
    """
    # Create the list of movie from our data
    return [MOVIE[key] for key in sorted(MOVIE.keys())]

def read_one(name):
    """
    This function responds to a request for /api/movie/{name}
    with one matching movie from MOVIE

    :param name:    name of movie to find
    :return:        movie details matching name
    """
    # Does the movie exist in MOVIE?
    if name in MOVIE:
        movie = MOVIE.get(name)

    # otherwise, nope, not found
    else:
        abort(
            404, "Movie with name {name} not found".format(name=name)
        )

    return movie


def create(movie):
    """
    This function creates a new movie in the MOVIE structure
    based on the passed in movie data

    :param movie:   movie to create in MOVIE structure
    :return:        201 on success, 406 on movie exists
    """
    popularity = movie.get("popularity", None)
    director = movie.get("director", None)
    genre = movie.get("genre", None)
    imdb_score = movie.get("imdb_score", None)
    name = movie.get("name", None)


    # Does the movie exist already?
    if name not in MOVIE and name is not None:
        MOVIE[name] = {
            "popularity": popularity,
            "director": director,
            "genre": genre,
            "imdb_score": imdb_score,
            "name": name,
        }
        return MOVIE[name], 201

    # Otherwise, they exist, that's an error
    else:
        abort(
            406,
            "Movie with name {name} already exists".format(name=name),
        )

def update(name, movie):
    """
    This function updates an existing movie in the MOVIE structure

    :param name:    name of movie to update in the MOVIE structure
    :param movie:   movie to update
    :return:        updated movie structure
    """
    # Does the movie exist in MOVIE?
    if name in MOVIE:
        MOVIE[name]["popularity"] = movie.get("popularity")
        MOVIE[name]["director"] = movie.get("director")
        MOVIE[name]["genre"] = movie.get("genre")
        MOVIE[name]["imdb_score"] = movie.get("imdb_score")
        MOVIE[name]["name"] = movie.get("name")

        return MOVIE[name]

    # otherwise, nope, that's an error
    else:
        abort(
            404, "Movie with name {name} not found".format(name=name)
        )

def delete(name):
    """
    This function deletes a movie from the MOVIE structure

    :param name:    name of movie to delete
    :return:        200 on successful delete, 404 if not found
    """
    # Does the movie to delete exist?
    if name in MOVIE:
        del MOVIE[name]
        return make_response(
            "{name} successfully deleted".format(name=name), 200
        )

    # Otherwise, nope, movie to delete not found
    else:
        abort(
            404, "Movie with name {name} not found".format(name=name)
        )
