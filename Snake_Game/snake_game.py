import random
import time
from turtle import Screen
from snake_class import *
from snake_food import *
from scoreboard import *

screen = Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.tracer(0)
screen.title("🐍- Snake Game - 🐍")

segment = Snake()
food = Food()
score = Score()

# * Game Initiation
game_is_on = True

# * Turtle Movement
screen.listen()
screen.onkey(segment.move_up, "Up")
screen.onkey(segment.move_down, "Down")
screen.onkey(segment.turn_left, "Left")
screen.onkey(segment.turn_right, "Right")

# * Game Loop
points = 0
score.show(points)
while game_is_on:
    screen.update()
    time.sleep(0.05)
    segment.move()

    # * Detect collision with food.
    if segment.head.distance(food) < 15:
        points += 1
        food.refresh()
        score.clear()
        segment.grow()
        score.show(points)

    # * Detect collision with boundaries.
    if (segment.head.xcor() > 280 or segment.head.xcor() < -280
            or segment.head.ycor() > 280 or segment.head.ycor() < -280):
        score.game_over()
        game_is_on = False

    # * Detect collision with self.
    for i in segment.segments[1:]:
        if segment.head.distance(i) < 5:
            score.game_over()
            game_is_on = False

screen.exitonclick()
