from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time



screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("sssnnnaaaake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
# screen.onkey(snake.pause, "space") TODO

game_is_on = True
while game_is_on:
    snake.move()
    screen.update()
    time.sleep(0.1)

    # detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.increment_score()
        snake.extend()
        food.refresh()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset_scoreboard()
        snake.reset_snake()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_scoreboard()
            snake.reset_snake()


screen.exitonclick()
