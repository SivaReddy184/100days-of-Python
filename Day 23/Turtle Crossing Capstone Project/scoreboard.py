from turtle import Turtle
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-250, 240)
        self.write(f"Level:{self.level}", align="center", font=FONT)

    def increase_score(self):
        self.clear()
        self.level += 1
        self.write(f"Level:{self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)

