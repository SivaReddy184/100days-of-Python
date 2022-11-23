from turtle import Turtle, Screen
import random

timmy = Turtle()


def shape(no_of_sides):
    angle = 360 / no_of_sides
    for i in range(no_of_sides):
        timmy.right(angle)
        timmy.forward(100)


for i in range(3, 11):
    shape(i)

screen = Screen()
screen.exitonclick()
