from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

API_KEY = ""
app = Flask(__name__)
app.config['SECRET_KEY'] = ''
Bootstrap5(app)

##CREATE DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy()
db.init_app(app)


##CREATE TABLE
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

with app.app_context():
    db.create_all()

class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")

class AddMovieForm(FlaskForm):
    title = StringField("Movie title")

@app.route("/")
def home():
    return render_template("index.html", movies = Movie.query.all())

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        url = "https://api.themoviedb.org/3/search/movie?include_adult=false&language=en-US&page=1"
        headers = {"api_key": API_KEY, "query":request.form['title']}
        response = requests.get(url, params=headers)
        response.raise_for_status()
        movies = response.json()['results']

        return render_template('select.html', options=movies)
    form = AddMovieForm()
    return render_template("add.html", form=form)

@app.route("/<int:movie>")
def add_to_db(movie):
    url = f"https://api.themoviedb.org/3/movie{movie}"
    response = requests.get(url, params={"api_key": API_KEY, "language": "en-US"})
    response.raise_for_status()
    movie_add = response.json()

    new_movie = Movie(
    title=movie_add['title'],
    year=movie_add['release_date'].split('-')[0],
    description=movie_add['overview'],
    rating=movie_add['vote_average'],
    ranking=0,
    review="...",
    img_url=f"https://image.tmdb.org/t/p/w500/{movie_add['poster_path']}"
    )
    db.session.add(new_movie)
    db.session.commit()
    return render_template("index.html", movies = Movie.query.all())

@app.route("/edit<int:id>", methods=['GET', 'POST'])
def edit(id):
    form = RateMovieForm()
    if request.method == "POST":
        movie = db.session.execute(db.select(Movie).where(Movie.id==id)).scalar()
        data = request.form
        movie.rating = data['rating']
        movie.review = data['review']
        db.session.commit()
    return render_template("edit.html", id=id, form=form)

@app.route("/delete<int:id>")
def delete(id):
    movie = db.session.execute(db.select(Movie).where(Movie.id==id)).scalar()
    db.session.delete(movie)
    db.session.commit()
    return render_template("index.html", movies = Movie.query.all())



if __name__ == '__main__':
    app.run(debug=True)