from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
screen.bgcolor("Cornsilk")
user_bet = screen.textinput("Choose your turtle! ", "Which turtle will win the race? Enter a color:  ")
turtles = []

colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "gray", "black"]
y_posiitons = [-100,-70, -40, -10, 20, 50, 80, 110, 140]

for index in range(0, 9):
  t = Turtle("turtle")
  t.color(colors[index])
  t.penup()
  t.goto(-230, y_posiitons[index])
  turtles.append(t)
  
if user_bet:
  race_is_on = True

while race_is_on:
  
  for i in turtles:
    if i.xcor() >= 230:
      if i.pencolor() == user_bet:
        print(f"You won the game! The winner color was {i.pencolor()}")
      else:
        print(f"You lose the game! The winner color was {i.pencolor()}")
      race_is_on = False

    i.forward(random.randint(0,10))
    
screen.exitonclick()
