from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(-270, 250)
        self.write(f"Level : {self.level}", align='left', font=('Arial', 18, 'bold'))
        self.hideturtle()

    def update_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level : {self.level}", align='left', font=('Arial', 18, 'bold'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Your Score :{self.level * 5}", align='center', font=('Arial', 20, 'bold'))
        self.goto(0, 20)
        self.write("GAME OVER", align='center', font=('Comic Sans Ms', 18, 'bold'))