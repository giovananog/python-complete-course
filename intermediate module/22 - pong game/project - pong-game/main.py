from turtle import Screen
from score import Score
from player import Player
from ball import Ball
from random import randint
import time


screen = Screen()

screen.bgcolor("black")
screen.screensize(600, 600)
screen.tracer(0)

player1 = Player(320, 0)
player2 = Player(-320, 0)
ball = Ball()
scoreboard = Score()
player1.up()
player2.up()

screen.listen()
screen.onkeypress(player1.up, "Up")
screen.onkeypress(player1.down, "Down")
screen.onkeypress(player2.up, "w")
screen.onkeypress(player2.down, "s")
screen.title("Pong")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    if ball.ycor() < -300 and ball.heading() > 90 and ball.heading() < 270:
        ball.setheading(randint(100, 160))
    elif ball.ycor() < -300:
        ball.setheading(randint(30, 70))
    if ball.ycor() > 300 and ball.heading() > 90 and ball.heading() < 270:
        ball.setheading(randint(190, 240))
    elif ball.ycor() > 300:
        ball.setheading(randint(290, 330))



    if ball.distance(player1.player) < 45 and player1.player.ycor() > 30:
        ball.setheading(randint(200, 260))
    elif ball.distance(player1.player) < 45 and player1.player.ycor() > 0:
        ball.setheading(randint(160, 220))
    elif ball.distance(player1.player) < 45 and player1.player.ycor() > -30:
        ball.setheading(randint(140, 200))
    elif ball.distance(player1.player) < 45 and player1.player.ycor() < 300:
        ball.setheading(randint(80, 160))
    

    if ball.distance(player2.player) < 45 and player2.player.ycor() > 30:
        ball.setheading(randint(280, 340))
    elif ball.distance(player2.player) < 45 and player2.player.ycor() > 0:
        ball.setheading(randint(30, 340))
    elif ball.distance(player2.player) < 45 and player2.player.ycor() > -30:
        ball.setheading(randint(0, 30))
    elif ball.distance(player2.player) < 45 and player2.player.ycor() < 300:
        ball.setheading(randint(30, 80))

    if ball.xcor() < -420:
        scoreboard.player1_score += 1
        scoreboard.print_score()
        ball.initial_left()

    if ball.xcor() > 420:
        scoreboard.player2_score += 1
        scoreboard.print_score()
        ball.initial_right()

    if scoreboard.player1_score == 5:
        game_is_on = False
        print("player 1 won the game! ")
    elif scoreboard.player2_score == 5:
        game_is_on = False
        print("player 2 won the game! ")

    ball.move()

print("done")
screen.exitonclick()