from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def finish_level(self):
        if self.ycor() > FINISH_LINE:
            self.goto(STARTING_POSITION)
            return True
        else:
            return False
