import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
directions = [0, 90, 180, 270]
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tuple_ = (r, g, b)
    return tuple_


for i in range(100):
    timmy.color(random_color())
    timmy.width(10)
    timmy.forward(20)
    timmy.setheading(random.choice(directions))
    timmy.speed(10)

screen = Screen()
screen.exitonclick()
