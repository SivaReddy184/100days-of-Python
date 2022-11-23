import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()

turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tuple_ = (r, g, b)
    return tuple_


timmy.speed("fastest")


def spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        timmy.color(random_color())
        timmy.setheading(timmy.heading() + size_of_gap)
        timmy.circle(100)


spirograph(5)
screen = Screen()
screen.exitonclick()
