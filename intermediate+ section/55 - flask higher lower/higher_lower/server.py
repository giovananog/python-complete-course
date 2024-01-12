from flask import Flask
from random import randint

number = randint(1, 10)
app = Flask(__name__)

@app.route('/')
def index():
    html = '<h1>Guess a number between 0 and 9</h1><img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'
    return html

@app.route('/<int:guess>')
def main(guess):
    if guess < number:
        html = '<h1>Too low, try again!</h1><img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    elif guess > number:
        html = '<h1>Too high, try again!</h1><img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    else:
        html = '<h1>You found me!</h1><img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    return html

if __name__ == "__main__":
    app.run(debug=True)