from turtle import Turtle, Screen, colormode
from random import choice
# import colorgram as cg
#
# new_colors = cg.extract("image.jpg", 30)
# colors_list = []
# for color in new_colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     colors_list.append((r, g, b))
#
# print(colors_list)

colors = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]
colormode(255)

t = Turtle()
t.speed("fastest")
t.hideturtle()
for i in range(10):
    t.penup()
    t.setposition(-300, ((-200)+(i*50)))
    for j in range(10):
        t.forward(50)
        t.pendown()
        t.dot(20, choice(colors))
        t.penup()

Screen().exitonclick()
