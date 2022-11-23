# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('hirst.jpg', 30)
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
import random
import turtle
from turtle import Turtle, Screen

timmy = Turtle()
turtle.colormode(255)
timmy.speed("fastest")
colors_list = [(154, 90, 48), (201, 157, 115), (42, 112, 146), (62, 115, 75), (244, 211, 84), (133, 171, 184),
               (195, 154, 30), (237, 65, 36), (130, 181, 137), (167, 11, 28), (148, 63, 87), (35, 173, 113),
               (144, 222, 155), (205, 132, 141), (229, 49, 58), (24, 51, 75), (249, 231, 1), (19, 89, 58),
               (246, 157, 147), (52, 150, 188), (180, 23, 13), (11, 72, 41), (244, 148, 157), (80, 76, 37),
               (5, 87, 114), (111, 4, 15)]
timmy.setheading(225)
timmy.penup()
timmy.hideturtle()
timmy.forward(300)
timmy.setheading(0)
for i in range(10):
    for i in range(10):
        timmy.dot(20, random.choice(colors_list))
        timmy.penup()
        timmy.forward(50)

    timmy.left(90)
    timmy.forward(50)
    timmy.left(90)
    timmy.forward(500)
    timmy.left(180)

screen = Screen()
screen.exitonclick()
