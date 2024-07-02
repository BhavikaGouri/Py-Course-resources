from turtle import Screen
from car_manager import Car
from player import Player
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.listen()

player = Player()
car = Car()
score = Scoreboard()

screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    car.create_cars()
    car.move()

    if player.finish_level():
        car.update_level()
        score.update_level()

    for cars in car.all_cars:
        if player.distance(cars) < 20:
            game_is_on = False
            score.game_over()
screen.exitonclick()
