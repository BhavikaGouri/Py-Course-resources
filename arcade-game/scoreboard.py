from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score_right = 0
        self.score_left = 0
        self.color('white')
        self.penup()
        self.goto(position)
        self.write(self.score_right, align='center', font=('Arial', 50, 'normal'))
        self.hideturtle()

    def update_score_right(self):
        self.clear()
        self.score_right += 1
        self.write(self.score_right, align='center', font=('Arial', 50, 'normal'))

    def update_score_left(self):
        self.clear()
        self.score_left += 1
        self.write(self.score_left, align='center', font=('Arial', 50, 'normal'))

