from flask import Blueprint, jsonify, render_template, send_file, request, current_app
from flask_wtf.csrf import generate_csrf
from flask_cors import cross_origin  # ✅ Import this
from .forms import MovieForm
from .models import Movie
from . import db
import os
from werkzeug.utils import secure_filename


main = Blueprint('main', __name__)  # Blueprint named "main"

@main.route('/')
def index():
    return jsonify(message="This is the beginning of our API")


@main.route('/api/v1/movies', methods=['POST'])
@cross_origin()  # ✅ Allow frontend to POST
def movies():
    form = MovieForm()

    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        poster = form.poster.data

        filename = secure_filename(poster.filename)
        poster.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

        new_movie = Movie(title=title, description=description, poster=filename)
        db.session.add(new_movie)
        db.session.commit()

        return jsonify({
            "message": "Movie Successfully added",
            "title": title,
            "poster": filename,
            "description": description
        }), 201

    return jsonify({"errors": form_errors(form)}), 400


@main.route('/api/v1/movies', methods=['GET'])
@cross_origin()  # ✅ Allow frontend to GET
def get_movies():
    movies = Movie.query.all()
    movie_list = []

    for movie in movies:
        movie_list.append({
            'id': movie.id,
            'title': movie.title,
            'description': movie.description,
            'poster': movie.poster,
            'created_at': movie.created_at.strftime('%Y-%m-%d %H:%M:%S')
        })

    return jsonify(movies=movie_list)


@main.route('/api/v1/csrf-token', methods=['GET'])
@cross_origin()  # ✅ Allow frontend to get CSRF
def get_csrf():
    return jsonify({'csrf_token': generate_csrf()})


def form_errors(form):
    error_messages = []
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            )
            error_messages.append(message)
    return error_messages


@main.route('/<file_name>.txt')
def send_text_file(file_name):
    file_dot_text = file_name + '.txt'
    return send_file(os.path.join(current_app.static_folder, file_dot_text))


@main.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@main.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
