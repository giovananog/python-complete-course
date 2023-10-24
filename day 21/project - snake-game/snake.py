from turtle import Turtle 
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
  
  def __init__(self):
    self.vector_snake = []
    self.initialize_snake()
    self.head = self.vector_snake[0]


  def initialize_snake(self):
    x = 0
    y = 0
    for _ in range(3): 
        snake = Turtle("square")
        snake.penup()
        snake.setposition(x,y)
        x -= 20
        snake.color("white")
        self.vector_snake.append(snake)

  def move(self):
    for i in range(len(self.vector_snake)-1, 0, -1):
      self.vector_snake[i].goto(self.vector_snake[i-1].xcor(), self.vector_snake[i-1].ycor())
    self.head.forward(MOVE_DISTANCE)

  def up(self):
    if self.head.heading() != DOWN:
      self.head.setheading(UP)

  def down(self):
    if self.head.heading() != UP:
      self.head.setheading(DOWN)

  def right(self):
    if self.head.heading() != LEFT:
      self.head.setheading(RIGHT)

  def left(self):
    if self.head.heading() != RIGHT:
      self.head.setheading(LEFT)

  def snake_grow(self):
    tale = self.vector_snake[-1]
    snake = Turtle("square")
    snake.penup()
    snake.goto(tale.xcor() - 20, tale.ycor())
    snake.color("white")
    self.vector_snake.append(snake)

  def colide_on_itself(self):
    for i in self.vector_snake[1:]:
        if self.head.distance(i) < 10:
          return True
    return False
  

  def colide_on_screen(self):
    if self.head.xcor() > 280 or self.head.xcor() < -300 or self.head.ycor() > 300 or self.head.ycor() < -280 :
      return True
    return False