import turtle as t
import random

race_start = False
all_turtle = []
screen = t.Screen()
screen.setup(width=500, height=400)
user = screen.textinput(title='Make Your Bet', prompt='Guess the color, which turtle will win?').lower()
color = ['violet', 'indigo', 'blue', 'green', 'yellow', 'red']

for i in range(1, 7):
    new_turtle = t.Turtle(shape='turtle')
    new_turtle.color(color[i-1])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100+(30*i))
    all_turtle.append(new_turtle)

if user in color:
    race_start = True

while race_start:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            winning_turtle = turtle.pencolor()
            race_start = False
            print("You won!") if user == turtle.pencolor() else print("You Lost!")
            print(f"{winning_turtle} is the winning turtle.")
        turtle.forward(random.randint(0, 10))

screen.exitonclick()
