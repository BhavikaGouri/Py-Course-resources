from ball import Ball
from player import Player
from scoreboard import Scoreboard
from turtle import Screen
import time

screen = Screen()
screen.tracer(0)
screen.bgcolor('black')
screen.title('Pong - The Arcade Game')
screen.setup(width=800, height=600)


left_player = Player((-350, 0))
right_player = Player((350, 0))
ball = Ball()
score_right = Scoreboard((100, 220))
score_left = Scoreboard((-110, 220))

screen.listen()
screen.onkey(left_player.go_up, "w")
screen.onkey(left_player.go_down, "s")
screen.onkey(right_player.go_up, "Up")
screen.onkey(right_player.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if (ball.distance(right_player) < 50 and ball.xcor() > 320) or (ball.distance(left_player) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() > 380:
        score_left.update_score_left()
        ball.goto(0, 0)
        ball.move_speed = 0.1
        ball.bounce_x()

    if ball.xcor() < -380:
        score_right.update_score_right()
        ball.goto(0, 0)
        ball.move_speed = 0.1
        ball.bounce_x()

    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    if score_left.score_left - score_right.score_right > 3:
        ball.game_is_over("Left player")
        game_is_on = False

    if score_right.score_right - score_left.score_left > 3:
        ball.game_is_over("Right player")
        game_is_on = False
        
screen.exitonclick()
