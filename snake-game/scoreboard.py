from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('black')
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))
