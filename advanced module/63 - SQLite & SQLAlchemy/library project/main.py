from flask import Flask, render_template, request, redirect, url_for
# import sqlite3
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db = SQLAlchemy()
db.init_app(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

with app.app_context():
    db.create_all()


with app.app_context():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()


@app.route('/')
def home():
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():

    if request.method == "POST":
        data = request.form
        new_book = Book(title=data['title'], author=data['author'], rating=data['rating'])
        db.session.add(new_book)
        db.session.commit()

        all_books = db.session.execute(db.select(Book).order_by(Book.title)).scalars()

        return render_template('index.html', books=all_books)
    return render_template('add.html')


@app.route("/delete<int:book_id>")
def delete(book_id):
    book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    db.session.delete(book_to_delete)
    db.session.commit()

    all_books = db.session.execute(db.select(Book).order_by(Book.title)).scalars()
    return render_template('index.html', books=all_books)

@app.route('/edit<int:id>', methods=['POST', 'GET'])
def change(id):
    book = db.session.execute(db.select(Book).where(Book.id==id)).scalar()
    if request.method == "POST":
        data = request.form
        book.rating = data['texto']
        db.session.commit()

        all_books = db.session.execute(db.select(Book).order_by(Book.title)).scalars()
        return render_template('index.html', books=all_books)

    return render_template('change_rating.html', book=book)


if __name__ == "__main__":
    app.run(debug=True)

