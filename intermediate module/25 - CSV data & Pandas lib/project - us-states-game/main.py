from turtle import Screen, Turtle
import pandas


screen = Screen()
screen.bgpic("blank_states_img.gif")

turtle = Turtle()
turtle.penup()
turtle.hideturtle()
turtle.goto(200, 200)
turtle.score = 0

data = pandas.read_csv("50_states.csv")
dict_data = data.to_dict()


def score_on_screen():
    turtle.clear()
    turtle.write(f"States: {turtle.score}/50", font=("Arial", 15, "normal"))

score_on_screen()

game_on = True

while game_on:
  guess = screen.textinput("Guess", "Write a state you know!")
  j = -1
  for i in dict_data['state']:
     j += 1
     if dict_data['state'][i].lower() == guess.lower():
        turtle.score += 1
        t = Turtle()
        t.hideturtle()
        t.penup()
        t.goto(dict_data['x'][j], dict_data['y'][j])
        t.write(guess)
        dict_data['state'][i] = ""
  score_on_screen()
  if turtle.score == 10: 
     game_on = False





screen.exitonclick()