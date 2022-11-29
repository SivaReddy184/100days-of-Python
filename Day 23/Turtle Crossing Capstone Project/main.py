import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=560)
screen.bgcolor("black")
screen.tracer(0)
player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()
    # Detect collision with car
    for car in cars.all_cars:
        if player.distance(car) < 30:
            game_is_on = False
            scoreboard.game_over()
    # if player is at finish line
    if player.reset_() is True:
        player.goto(0, -260)
        cars.level_up()
        scoreboard.increase_score()

screen.exitonclick()
