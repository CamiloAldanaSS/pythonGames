import time
from turtle import Turtle, Screen
from paddle_class import Paddle
from ball_class import Ball
from scoreboard import Scoreboard

STARTING_POSITIONS = [(370, 0), (-380, 0)]
COLORS = ["blue", "red"]

# * Screen Creation * #
screen = Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)
# * ---------------- * #

# * Paddles Creation * #
paddle_r = Paddle(STARTING_POSITIONS[0], COLORS[0])  # Right Paddle
paddle_l = Paddle(STARTING_POSITIONS[1], COLORS[1])  # Left Paddle
# * ---------------- * #

# * Scoreboard Creation * #
score = Scoreboard()
# * ---------------- * #

# * Ball Creation * #
ball = Ball()
# * ---------------- * #

# * Movements * #
screen.onkeypress(paddle_r.move_paddle_down, "Down")
screen.onkeypress(paddle_l.move_paddle_up, "w")
screen.onkeypress(paddle_l.move_paddle_down, "s")
screen.onkeypress(paddle_r.move_paddle_up, "Up")
# * ---------------- * #

# * Game Initiation * #
game_on = True
screen.listen()
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    score.show()

    # * Ball Collision With Wall * #
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_wall()
    # * ---------------- * #

    # * Ball Collision With Paddles * #
    if (ball.xcor() > 330 and ball.distance(paddle_r) < 60) or (ball.xcor() < -350 and ball.distance(paddle_l) < 60):
        ball.bounce_x()
    # * ---------------- * #

    # * Score Update * #
    if ball.xcor() > 380:
        score.update_score("l")
        score.show()
        ball.reset_position()

    if ball.xcor() < -380:
        score.update_score("r")
        score.show()
        ball.reset_position()
    # * ---------------- * #

screen.exitonclick()
