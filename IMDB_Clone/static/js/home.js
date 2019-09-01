/*
 * JavaScript file for the application to demonstrate
 * using the API
 */

// Create the namespace instance
let ns = {};

// Create the model instance
ns.model = (function() {
    'use strict';

    let $event_pump = $('body');

    // Return the API
    return {
        'read': function() {
            let ajax_options = {
                type: 'GET',
                url: 'api/movie',
                accepts: 'application/json',
                dataType: 'json'
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_read_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        },
        create: function(popularity, director, genre, imdb_score, name) {
            let ajax_options = {
                type: 'POST',
                url: 'api/movie',
                accepts: 'application/json',
                contentType: 'application/json',
                dataType: 'json',
                data: JSON.stringify({
                    'popularity': popularity,
                    'director': director,
                    'genre': genre,
                    'imdb_score': imdb_score,
                    'name': name
                })
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_create_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        },
        update: function(popularity, director, genre, imdb_score, name, movie_id) {
            let ajax_options = {
                type: 'PUT',
                url: 'api/movie/' + movie_id,
                accepts: 'application/json',
                contentType: 'application/json',
                dataType: 'json',
                data: JSON.stringify({
                  'popularity': popularity,
                  'director': director,
                  'genre': genre,
                  'imdb_score': imdb_score,
                  'name': name
                })
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_update_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        },
        'delete': function(name) {
            let ajax_options = {
                type: 'DELETE',
                url: 'api/movie/' + name,
                accepts: 'application/json',
                contentType: 'plain/text'
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_delete_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        },
    };
}());

// Create the view instance
ns.view = (function() {
    'use strict';

    let $popularity = $('#popularity'),
        $director = $('#director'),
        $genre = $('#genre'),
        $imdb_score = $('#imdb_score'),
        $movie_id = $('#movie_id'),
        $name = $('#name');

    // return the API
    return {
        reset: function() {
            $popularity.val('');
            $director.val('');
            $genre.val('');
            $imdb_score.val('');
            $movie_id.val('');
            $name.val('').focus();
        },
        update_editor: function(popularity, director, genre, imdb_score, name, movie_id) {
            $popularity.val(popularity);
            $director.val(director);
            $genre.val(genre);
            $imdb_score.val(imdb_score);
            $movie_id.val(movie_id);
            $name.val(name).focus();
        },
        build_table: function(movie) {
            let rows = ''

            // clear the table
            $('.movie table > tbody').empty();

            // did we get a movie array?
            if (movie) {
                for (let i=0, l=movie.length; i < l; i++) {
                    rows += `<tr><td class="movie_id">${movie[i].movie_id}</td><td class="popularity">${movie[i].popularity}</td><td class="director">${movie[i].director}</td><td class="genre">${movie[i].genre}</td><td class="imdb_score">${movie[i].imdb_score}</td><td class="name">${movie[i].name}</td></tr>`;
                }
                $('table > tbody').append(rows);
            }
        },
        error: function(error_msg) {
            $('.error')
                .text(error_msg)
                .css('visibility', 'visible');
            setTimeout(function() {
                $('.error').css('visibility', 'hidden');
            }, 3000)
        }
    };
}());

// Create the controller
ns.controller = (function(m, v) {
    'use strict';

    let model = m,
        view = v,
        $event_pump = $('body'),
        $popularity = $('#popularity'),
        $director = $('#director'),
        $genre = $('#genre'),
        $imdb_score = $('#imdb_score'),
        $movie_id = $('#movie_id'),
        $name = $('#name');

    // Get the data from the model after the controller is done initializing
    setTimeout(function() {
        model.read();
    }, 100)

    // Validate input
    function validate(popularity, director, genre, imdb_score, name) {
        return popularity !== "" && director !== "" && genre !== "" && imdb_score !== "" && name !== "";
    }

    // Create our event handlers
    $('#create').click(function(e) {
        let popularity = $popularity.val(),
            director = $director.val(),
            genre = $genre.val(),
            imdb_score = $imdb_score.val(),
            name = $name.val();

        e.preventDefault();
        // console.log('Create clicked ',popularity,director, genre, imdb_score, name)
        if (validate(popularity, director, genre, imdb_score, name)) {
            model.create(popularity, director, genre, imdb_score, name)
        } else {
            alert('Problem with first or last name input');
        }
    });

    $('#update').click(function(e) {
        let popularity = $popularity.val(),
            director = $director.val(),
            genre = $genre.val(),
            imdb_score = $imdb_score.val(),
            name = $name.val(),
            movie_id = $movie_id.val();

        e.preventDefault();
        console.log('Update clicked ',popularity,director, genre, imdb_score, name, movie_id)
        if (validate(popularity, director, genre, imdb_score, name)) {
            model.update(popularity, director, genre, imdb_score, name, movie_id)
        } else {
            alert('Problem with first or last name input');
        }
        e.preventDefault();
    });

    $('#delete').click(function(e) {
        let name = $name.val();

        e.preventDefault();

        if (validate('placeholder', 'placeholder', 'placeholder', 'placeholder', name)) {
            model.delete(name)
        } else {
            alert('Problem with first or last name input');
        }
        e.preventDefault();
    });

    $('#reset').click(function() {
        view.reset();
    })

    $('table > tbody').on('dblclick', 'tr', function(e) {
        let $target = $(e.target),
            popularity,
            director,
            genre,
            imdb_score,
            name,
            movie_id;

        popularity = $target
            .parent()
            .find('td.popularity')
            .text();

        director = $target
            .parent()
            .find('td.director')
            .text();

        genre = $target
            .parent()
            .find('td.genre')
            .text();

        imdb_score = $target
            .parent()
            .find('td.imdb_score')
            .text();

        name = $target
            .parent()
            .find('td.name')
            .text();

        movie_id = $target
            .parent()
            .find('td.movie_id')
            .text();


        view.update_editor(popularity, director, genre, imdb_score, name, movie_id);
    });

    // Handle the model events
    $event_pump.on('model_read_success', function(e, data) {
        view.build_table(data);
        view.reset();
    });

    $event_pump.on('model_create_success', function(e, data) {
        model.read();
    });

    $event_pump.on('model_update_success', function(e, data) {
        model.read();
    });

    $event_pump.on('model_delete_success', function(e, data) {
        model.read();
    });

    $event_pump.on('model_error', function(e, xhr, textStatus, errorThrown) {
        let error_msg = textStatus + ': ' + errorThrown + ' - ' + xhr.responseJSON.detail;
        view.error(error_msg);
        console.log(error_msg);
    })
}(ns.model, ns.view));
