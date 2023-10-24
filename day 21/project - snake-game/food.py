from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
       super().__init__()
       self.shape("circle")
       self.penup()
       self.shapesize(0.5, 0.5)
       self.color("blue")
       self.speed("fastest")
       self.random_place()


    def random_place(self):
       random_x = random.randint(-280, 280)
       random_y = random.randint(-280, 280)
       self.goto(random_x, random_y)
