from turtle import Turtle

class Player():

    def __init__(self, x, y):
        self.player = self.new_player()
        self.player.goto(x, y)

    def new_player(self):
        player = Turtle("square")
        player.penup()
        player.color("white")
        player.turtlesize(1, 5)
        return player

    def down(self):
      if self.player.ycor() > -300:
        self.player.setheading(270)
        self.player.forward(35)
    
    def up(self):
     if self.player.ycor() < 300:
        self.player.setheading(90)
        self.player.forward(35)
