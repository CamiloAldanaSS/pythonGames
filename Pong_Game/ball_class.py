import random
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.dx = 10
        self.dy = 10
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(0.8, 0.8)
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.dy *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.1

    def bounce_x(self):
        self.dx *= -1
        self.move_speed *= 0.9