from turtle import Turtle
STARTING_POSITION = (0, -260)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 270


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.color("white")
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def reset_(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
