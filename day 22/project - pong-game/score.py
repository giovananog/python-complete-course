from turtle import Turtle


class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.player1_score = 0
        self.player2_score = 0
        self.dots_on_screen()
        self.print_score()

    def dots_on_screen(self):
        x = 0
        y = -280
        for i in range(15):
          dot = Turtle("square")
          dot.penup()
          dot.color("white")
          dot.goto(x, y)
          y += 40

    def print_score(self):
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-60, 250)
        self.clear()
        self.write(self.player2_score, align="center", font=("Arial", 50, "normal"))
        self.goto(60, 250)
        self.write(self.player1_score, align="center", font=("Arial", 50, "normal"))