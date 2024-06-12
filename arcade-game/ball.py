from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.penup()
        self.y_move = 7
        self.x_move = 7
        self.move_speed = 0.1

    def move(self):
        self.speed(self.move_speed)
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.2
        self.move()

    def game_is_over(self, winner):
        self.goto(0, 0)
        self.write(f" GAME OVER\n{winner} is the Winner", align='center', font=('Arial', 30, 'bold'))
