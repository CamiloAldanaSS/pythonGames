import random
import turtle
from turtle import Turtle

from Intermediate.Section_22_Build_Pong.paddle_class import MOVE_DISTANCE

COLOR_LIST = [(140, 163, 192), (46, 104, 160), (217, 155, 107), (188, 153, 174), (243, 232, 236), (135, 69, 102),
              (133, 179, 146), (109, 108, 174), (146, 79, 56), (221, 195, 133),
              (207, 83, 122), (83, 162, 107), (41, 157, 189), (89, 133, 112), (181, 23, 53), (231, 137, 17),
              (237, 66, 36), (55, 57, 115), (208, 179, 189), (161, 210, 171), (230, 174, 165), (52, 50, 61),
              (144, 206, 225), (57, 47, 55), (188, 188, 202), (72, 49, 44), (84, 56, 49)]
STARTING_MOVING_DISTANCE = 5
MOVE_INCREMENT = 5


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVING_DISTANCE


    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            turtle.colormode(255)
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(COLOR_LIST))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
