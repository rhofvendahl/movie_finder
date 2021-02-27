from flask import Flask, jsonify, request, redirect, url_for
from scripts import mock

app = Flask(__name__)

@app.route("/find-movies-mock")
def find_movies_mock():
    keywords = request.args.get("keywords")
    description = request.args.get("description")

    if keywords:
        movies = mock.get_movies_from_keywords(keywords)
    elif description:
        movies = mock.get_movies_from_description(description)
    else:
        return "", 418

    movies_json = jsonify(movies)
    return movies_json, 200

@app.route("/find-movies")
def find_movies():
    redirect_url = url_for('find_movies_mock') + "?" + request.query_string.decode()
    return redirect(redirect_url)

if __name__ == "__main__":
    app.run()
