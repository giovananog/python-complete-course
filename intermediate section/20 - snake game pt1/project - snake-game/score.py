from turtle import Turtle

class Score(Turtle):

    def __init__(self):
         super().__init__()
         self.pontuation = 0
         self.hideturtle()
         self.color("white")
         self.penup()
         self.goto(0, 260)
    
    def show_pontuation(self):
        self.clear()
        self.write(f"Score: {self.pontuation}", align="center", font=("Arial", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER. ", align="center", font=("Arial", 16, "normal"))