from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(0, 270)
        self.score = 0

    def show(self, amount):
        self.write(f"Level: {amount}", False, "center", ('Arial', 20, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", ('Monserrat', 30, 'normal'))

    def update_score(self):
        self.show(self.score)
        self.score += 1
        self.clear()

