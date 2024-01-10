from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def move_forwards():
  t.forward(10)

def move_backwards():
  t.setheading(180)
  t.forward(10)

def turn_right():
  t.setheading(t.heading() + 10)
  t.forward(10)

def turn_left():
  t.setheading(t.heading() - 10)
  t.forward(10)

def clear_screen():
  t.clear()
  t.penup()
  t.home()
  t.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_right)
screen.onkey(key="d", fun=turn_left)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()

 
