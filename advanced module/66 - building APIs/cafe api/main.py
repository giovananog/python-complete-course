from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


# with app.create_content():
#     db.create_all()


@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record

@app.route("/random")
def get_random_cafe():
    cafe = db.session.execute(db.select(Cafe))
    all_cafe = cafe.scalars().all()
    random_cafe = choice(all_cafe)
    return jsonify(cafe={ 
            "name":random_cafe.name,
            "id":random_cafe.id,
            "map_url":random_cafe.map_url,
            "img_url":random_cafe.img_url,
            "location":random_cafe.location,
            "seats":random_cafe.seats,
            "has_toilet":random_cafe.has_toilet,
            "has_wifi":random_cafe.has_wifi,
            "has_sockets":random_cafe.has_sockets,
            "can_take_calls":random_cafe.can_take_calls,
            "coffee_price":random_cafe.coffee_price,
            })

@app.route("/all")
def get_all_cafe():
    cafe_records = db.session.query(Cafe).all()
    all_cafe = []

    for coffee in cafe_records:
        cafe_data = { 
            "name": coffee.name,
            "id": coffee.id,
            "map_url": coffee.map_url,
            "img_url": coffee.img_url,
            "location": coffee.location,
            "seats": coffee.seats,
            "has_toilet": coffee.has_toilet,
            "has_wifi": coffee.has_wifi,
            "has_sockets": coffee.has_sockets,
            "can_take_calls": coffee.can_take_calls,
            "coffee_price": coffee.coffee_price,
        }
        all_cafe.append(cafe_data)

    return jsonify(cafe=all_cafe)

@app.route("/search")
def search():
    name = request.args.get("loc")
    cafes = db.session.execute(db.select(Cafe).where(Cafe.location == name))
    all_cafes = cafes.scalars().all()
    all_cafe = []

    for coffee in all_cafes:
        cafe_data = { 
            "name": coffee.name,
            "id": coffee.id,
            "map_url": coffee.map_url,
            "img_url": coffee.img_url,
            "location": coffee.location,
            "seats": coffee.seats,
            "has_toilet": coffee.has_toilet,
            "has_wifi": coffee.has_wifi,
            "has_sockets": coffee.has_sockets,
            "can_take_calls": coffee.can_take_calls,
            "coffee_price": coffee.coffee_price,
        }
        all_cafe.append(cafe_data)

    if all_cafes == []:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404
    return jsonify(cafe=all_cafe)


## HTTP POST - Create Record

@app.route("/add", methods=['POST'])
def add():
    new = Cafe(
    name = request.args.get("name"),
    id = request.args.get("id"),
    map_url = request.args.get("map_url"),
    img_url = request.args.get("img_url"),
    location = request.args.get("location"),
    seats = request.args.get("seats"),
    has_toilet = request.args.get("has_toilet"),
    has_wifi = request.args.get("has_wifi"),
    has_sockets = request.args.get("has_sockets"),
    can_take_calls = request.args.get("can_take_calls"),
    coffee_price = request.args.get("coffee_price"),
    )
    db.session.add(new)
    db.session.commit()
    return jsonify(message={"Success": "The DataBase was succefully updated!"})

## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<cafe_id>", methods=['PATCH'])
def update(cafe_id):
    book_to_update = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
    book_to_update.coffee_price = request.args.get("coffee_price")
    db.session.commit()
    return jsonify(message={"Success": "The DataBase was succefully updated!"})


## HTTP DELETE - Delete Record
@app.route("/report-closed/<cafe_id>", methods=['DELETE'])
def remove(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        cafe = db.get_or_404(Cafe, cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403

if __name__ == '__main__':
    app.run(debug=True)
