from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("/Users/bhavikagouri/Py-Course-resources/snake-game-HighScore/newdata.txt") as data:
            self.high_score = int(data.read())
        self.color('black')
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score} -- HighScore: {self.high_score}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score} -- HighScore: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score

        with open("data.txt", mode="w") as data:
            data.write(f"{self.high_score}")

        self.score = 0
        self.clear()
        self.write(f"Score: {self.score} -- HighScore: {self.high_score}", align="center", font=("Arial", 24, "normal"))

