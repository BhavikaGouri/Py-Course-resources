from turtle import Turtle
import random
COLOURS = ['red', 'blue', 'pink', 'green', 'yellow', 'purple', 'orange']


class Car:
    def __init__(self):
        self.all_cars = []
        self.move_distance = 10

    def create_cars(self):
        random_choice = random.randint(1, 6)
        if random_choice == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            random_y = random.randint(-250, 250)
            new_car.color(random.choice(COLOURS))
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.move_distance)

    def update_level(self):
        self.move_distance += 10
