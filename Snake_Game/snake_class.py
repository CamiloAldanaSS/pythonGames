from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def grow(self):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("grey")
        new_segment.hideturtle()
        self.segments.append(new_segment)

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("grey")
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            self.segments[segment].showturtle()
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    # ! Movements
    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

