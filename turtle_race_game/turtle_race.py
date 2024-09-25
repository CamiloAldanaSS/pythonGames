import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(500, 400)

colors = ["red", "blue", "green", "orange", "purple"]
turtles = []


def create_turtles():
    color_count = 0
    for turtle in range(0, 5):
        turtle = Turtle()
        turtle.shape("turtle")
        turtle.color(colors[color_count])
        color_count += 1
        turtles.append(turtle)


def start_position():
    x = -200
    y = -150
    for turtle_new in turtles:
        turtle_new.penup()
        y += 50
        turtle_new.goto(x=x, y=y)


def start_race():
    pass


create_turtles()
start_position()
start_race()

bet = screen.textinput("Make your bet!!", "Which turtle will win? Enter the color:").lower()

if bet:
    is_race_on = True

while is_race_on:
    random_distance = random.randint(0, 10)
    turtle = random.choice(turtles)
    turtle.forward(random_distance)
    if turtle.xcor() > 230:
        is_race_on = False
        print(f"The winner is the {turtle.pencolor()} turtle!!")
        if bet == turtle.pencolor():
            print("You won!! 🏅🏆")
        else:
            print("You've lost!!  😢😢😢 ")

screen.exitonclick()
