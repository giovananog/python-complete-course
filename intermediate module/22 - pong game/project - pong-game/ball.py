from turtle import Turtle
from random import randint

class Ball(Turtle):

    def __init__(self):
        super().__init__("square")
        self.color("white")
        self.speed(10)
        self.penup()
        self.setheading(0)

    def initial_left(self):
        self.goto(0,0)
        self.setheading(randint(140, 200))
    
    def initial_right(self):
        self.goto(0,0)
        self.setheading(randint(40, 300))
    
    def move(self):
        self.forward(30)