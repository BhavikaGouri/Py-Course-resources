from turtle import Turtle, Screen
import turtle as t
import random

tin = Turtle()
tin.shape('turtle')
t.colormode(255)
tin.speed('fastest')


def give_colour():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    return r, b, g


def draw(size):
    for i in range(int(360/size)):
        tin.color(give_colour())
        tin.circle(100)
        tin.setheading(tin.heading()+size)


draw(2)
my_screen = Screen()
my_screen.exitonclick()
