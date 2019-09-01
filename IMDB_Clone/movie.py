"""
This is the movie module and supports all the ReST actions for the
MOVIE collection
"""

# System modules
from datetime import datetime

# 3rd party modules
from flask import make_response, abort
from config import db
from models import Movie, MovieSchema

# Data to serve with our API
# MOVIE = {
#   "The Wizard of Oz":{
#     "popularity": 83.0,
#     "director": "Victor Fleming",
#     "genre": [
#       "Adventure",
#       " Family",
#       " Fantasy",
#       " Musical"
#     ],
#     "imdb_score": 8.3,
#     "name": "The Wizard of Oz"
#   },
#   "Star Wars":{
#     "popularity": 88.0,
#     "director": "George Lucas",
#     "genre": [
#       "Action",
#       " Adventure",
#       " Fantasy",
#       " Sci-Fi"
#     ],
#     "imdb_score": 8.8,
#     "name": "Star Wars"
#   },
#   "Cabiria":{
#     "popularity": 66.0,
#     "director": "Giovanni Pastrone",
#     "genre": [
#       "Adventure",
#       " Drama",
#       " War"
#     ],
#     "imdb_score": 6.6,
#     "name": "Cabiria"
#   },
# }


def read_all():
    """
    This function responds to a request for /api/movie
    with the complete lists of movie

    :return:        json string of list of movie
    """
    # Create the list of movie from our data
    #return [MOVIE[key] for key in sorted(MOVIE.keys())]
    movie = Movie.query.order_by(Movie.name).all()
    # Serialize the data for the response
    movie_schema = MovieSchema(many=True)
    data = movie_schema.dump(movie)#.data
    return data

def read_one(movie_id):
    """
    This function responds to a request for /api/movie/{movie_id}
    with one matching movie from MOVIE

    :param movie_id:    Id of movie to find
    :return:            movie details matching id
    """

    # Get the movie requested
    movie = Movie.query.filter(Movie.movie_id == movie_id).one_or_none()

    # Did we find a person?
    if movie is not None:
        # Serialize the data for the response
        movie_schema = MovieSchema()
        data = movie_schema.dump(movie)#.data
        return data

    # otherwise, nope, not found
    else:
        abort(
            404, "Movie not found for Id: {movie_id}".format(movie_id=movie_id)
        )

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

    existing_movie = (
        Movie.query.filter(Movie.name == name)
        .one_or_none()
    )
    if existing_movie is None:
        # Create a person instance using the schema and the passed in person
        schema = MovieSchema()
        new_movie = schema.load(movie, session=db.session)#.data
        # Add the person to the database
        db.session.add(new_movie)
        db.session.commit()
        # Serialize and return the newly created person in the response
        data = schema.dump(new_movie)#.data
        return data, 201



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

def update(movie_id, movie):
    """
    This function updates an existing movie in the MOVIE structure

    :param movie_id:    Id of movie to update in the MOVIE structure
    :param movie:       movie to update
    :return:            updated movie structure
    """

    # Get the person requested from the db into session
    update_movie = Movie.query.filter(
        Movie.movie_id == movie_id
    ).one_or_none()

    # Try to find an existing movie with the same name as the update
    name = movie.get("name")

    existing_movie = (
        Movie.query.filter(Movie.name == name)
        .one_or_none()
    )

    # Are we trying to find a movie that does not exist?
    if update_movie is None:
        abort(
            404,
            "Movie not found for Id: {movie_id}".format(movie_id=movie_id),
        )

    # Would our update create a duplicate of another person already existing?
    elif (
        existing_movie is not None and existing_movie.movie_id != movie_id
    ):
        abort(
            409,
            "Movie \"{name}\" exists already".format(name=name),
        )


    # Otherwise go ahead and update!
    else:

        # turn the passed in person into a db object
        schema = MovieSchema()
        update = schema.load(movie, session=db.session)#.data

        # Set the id to the person we want to update
        update.movie_id = update_movie.movie_id

        # merge the new object into the old and commit it to the db
        db.session.merge(update)
        db.session.commit()

        # return updated person in the response
        data = schema.dump(update_movie)#.data

        return data, 200

def delete(movie_id):
    """
    This function deletes a movie from the MOVIE structure

    :param movie_id:    name of movie to delete
    :return:            200 on successful delete, 404 if not found
    """
    # Get the person requested
    movie = Movie.query.filter(Movie.movie_id == movie_id).one_or_none()

    # Did we find a person?
    if movie is not None:
        db.session.delete(movie)
        db.session.commit()
        return make_response(
            "Movie Id: {movie_id} deleted".format(movie_id=movie_id), 200
        )

    # Otherwise, nope, movie to delete not found
    else:
        abort(
            404, "Movie for Id: {movie_id} not found".format(movie_id=movie_id)
        )
