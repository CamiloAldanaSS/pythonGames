from turtle import Turtle

MOVE_DISTANCE = 40

class Paddle(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.shape("square")
        self.goto(position)
        self.color(color)

    def move_paddle_up(self):
        new = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new)

    def move_paddle_down(self):
        new = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new)




