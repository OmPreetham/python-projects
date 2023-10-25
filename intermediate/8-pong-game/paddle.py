from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape(name="square")
        self.color("white")
        # self.shapesize(stretch_wid=5, stretch_len=1)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)
        self.penup()
        self.goto(position)

    def go_up(self):
        # new_y = self.ycor() + 20
        # self.goto(self.xcor(), new_y)
        self.forward(20)

    def go_down(self):
        # new_y = self.ycor() - 20
        # self.goto(self.xcor(), new_y)
        self.forward(-20)


