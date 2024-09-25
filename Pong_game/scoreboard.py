from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.l_score = 0
        self.r_score = 0

    def show(self):
        self.clear()
        self.goto(-100, 240)
        self.write(self.l_score, align="center", font=("Courier", 50, "normal"))
        self.goto(100, 240)
        self.write(self.r_score, align="center", font=("Courier", 50, "normal"))

    def update_score(self, pos):
        if pos == "l":
            self.l_score += 1
        else:
            self.r_score += 1

