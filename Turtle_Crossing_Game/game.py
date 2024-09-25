import time
from turtle import Screen

from scoreboard import Score
from car_class import Car
from player import Player

# ! Screen Creation ! #
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
# ! --------------- ! #

# ! Player Creation ! #
player = Player()
# ! --------------- ! #

# ! Scoreboard Creation ! #
score = Score()
# ! --------------- ! #

# ! Cars Creation ! #
car = Car()
car.hideturtle()
# ! --------------- ! #

# ! Player Movement ! #
screen.listen()
screen.onkey(player.move, "Up")
# ! --------------- ! #

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_cars()
    car.move_cars()
    score.show(score.score)

    for carr in car.all_cars:
        if player.distance(carr) < 20:
            score.game_over()
            game_is_on = False

    if player.ycor() > 280:
        score.update_score()
        player.reset()
        car.increase_speed()

screen.exitonclick()
