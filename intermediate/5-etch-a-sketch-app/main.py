from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
screen.listen()


def move_forward():
    t.forward(10)


def move_backward():
    t.backward(10)


def turn_left():
    t.left(10)


def turn_right():
    t.right(10)


def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_right, "a")
screen.onkey(turn_left, "d")
screen.onkey(clear, "c")

screen.exitonclick()