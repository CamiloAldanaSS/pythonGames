from turtle import Turtle
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)

    def show(self, amount):
        self.write(f"Score: {amount}", False, "center", ('Arial', 20, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", ('Monserrat', 30, 'normal'))