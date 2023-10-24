from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(600, 600)
screen.title("Snake Game!")
screen.bgcolor("black")
screen.tracer(0)


snake = Snake()
food = Food()
score = Score()


screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")


game_is_on = True  
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    score.show_pontuation()
    if snake.head.distance(food) < 15:
      food.random_place()
      snake.snake_grow()
      score.pontuation += 1
    if snake.colide_on_screen():
      game_is_on = False
      score.game_over()
    if snake.colide_on_itself():
      game_is_on = False
      score.game_over()
  

screen.exitonclick()