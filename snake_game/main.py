from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score_Board
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score_Board()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    if snake.head.distance(food) < 15:
        snake.extend()
        score.food_eaten()
        food.refresh()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()
    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 10:
            score.game_over()
            game_is_on = False

    snake.move()

screen.exitonclick()
