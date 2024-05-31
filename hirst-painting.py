# import colorgram as cl
import turtle
import random

# rgb_colors = []
# colors = cl.extract("image.jpg", 30)
# for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    rgb_colors.append(new_color)
# print(rgb_colors)

list_colors = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123),
                   (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86),
                   (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
                   (54, 45, 50),  (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89),
                   (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
                   (176, 192, 208), (168, 99, 102)]

tin = turtle.Turtle()
tin.speed('fastest')
tin.penup()
tin.hideturtle()

turtle.colormode(255)
tin.setheading((270+180)/2)
tin.forward(300)
tin.setheading(0)

for i in range(1, 11):
    for _ in range(10):
        k = random.choice(list_colors)
        tin.dot(20, k)
        tin.color(k)
        tin.forward(40)
    if i % 2 != 0 or i == 1:
        for _ in range(2):
            tin.left(90)
            tin.forward(40)
    else:
        for _ in range(2):
            tin.right(90)
            tin.forward(40)

my_screen = turtle.Screen()
my_screen.exitonclick()
