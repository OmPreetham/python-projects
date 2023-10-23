from random import randint
from turtle import Turtle, Screen, colormode
colormode(255)
screen = Screen()

screen.setup(width=1000, height=1000)
user_choice = screen.textinput(title="Guess the Winner ", prompt="Who will win the race? ")
y_position = [-200, -100, 0, 100, 200]
colors = ["red", "yellow", "orange", "pink", "purple", "blue"]
turtles = []
for turtle in range(0, 5):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle])
    new_turtle.setposition(x=-450, y=y_position[turtle])
    turtles.append(new_turtle)

race_on = True

while race_on:
    for turtle in turtles:
        if turtle.xcor() >= 990:
            race_on = False
            winner = turtle.pencolor()
            if winner == user_choice:
                print(f"Yey!!! You Win, {winner} crossed the line first. ")
            else:
                print(f"You Lost, {winner} crossed the line first. ")
        turtle.forward(randint(10,20))


screen.exitonclick()