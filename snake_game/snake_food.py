import random
import turtle
from turtle import Turtle
color_list = [(140, 163, 192), (46, 104, 160), (217, 155, 107), (188, 153, 174),
              (243, 232, 236), (135, 69, 102), (133, 179, 146), (109, 108, 174), (146, 79, 56), (221, 195, 133),
              (207, 83, 122), (83, 162, 107), (41, 157, 189), (89, 133, 112), (181, 23, 53), (231, 137, 17),
              (237, 66, 36), (55, 57, 115), (208, 179, 189), (161, 210, 171), (230, 174, 165), (52, 50, 61),
              (144, 206, 225), (57, 47, 55), (188, 188, 202), (72, 49, 44), (84, 56, 49)]


class Food(Turtle):
    def __init__(self):
        super().__init__()
        turtle.colormode(255)
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color(random.choice(color_list))
        self.refresh()

    def refresh(self):
        self.color(random.choice(color_list))
        self.goto(random.randint(-280, 280), random.randint(-280, 280))



