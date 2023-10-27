from turtle import Screen, Turtle
import pandas

df = pandas.read_csv("50_states.csv")

screen = Screen()
screen.title("U.S. States Quiz Game")
screen.bgpic("blank_states_img.gif")
screen.setup(725, 491)

t = Turtle()
t.penup()
t.hideturtle()

states = df["state"].tolist()
guessed_states = []

while len(guessed_states) < 51:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 Guessed States", prompt="What's the next State?").title()
    if answer in states:
        state = df[df.state == answer].to_dict()
        x_coordinate = list(state["x"].items())[0][1]
        y_coordinate = list(state["y"].items())[0][1]
        t.goto(x_coordinate, y_coordinate)
        t.write(answer)
        guessed_states.append(answer)
        states.remove(answer)
    elif answer == "Exit":
        pandas.DataFrame(states).to_csv("states_to_learn.csv")
        break
