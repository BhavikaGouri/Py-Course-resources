from food import Food
from scoreboard import Scoreboard
from snake import Snake
import turtle as t
import time

screen = t.Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.bgcolor('dark green')
screen.title('The Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.new_food()
        snake.add_tail()
        score.update_score()

    if snake.detect_game_over():
        score.reset_game()
        snake.reset_game()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset_game()
            snake.reset_game()


score.game_over()
screen.exitonclick()
