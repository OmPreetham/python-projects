from turtle import Turtle

FONT = ('Arial', 30, 'normal')
ALIGNMENT = "center"
POSITION = (0, 250)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(POSITION)
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def increase_l_score(self):
        self.l_score += 1
        self.update_score()

    def increase_r_score(self):
        self.r_score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.l_score}      {self.r_score}", align=ALIGNMENT, font=FONT)