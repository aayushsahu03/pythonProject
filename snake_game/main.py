import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0)
game_is_on = True


snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.reset, 'Return')

score = Score()

while game_is_on:
    screen.update()
    time.sleep(0.075)
    snake.move()

    # detect food
    if snake.head.distance(food) < 20:
        # print("nom nom nom")
        score.update_score()
        food.refresh()
        snake.extend()

    # collision with wall
    if snake.head.xcor()>285 or snake.head.xcor()<-285\
        or snake.head.ycor()>285 or snake.head.ycor()<-285:
        
        score.game_over()
        score.reset()
        snake.reset()

    # detect collision with itself
    for seg in snake.segments[1:]:
        if snake.head.distance(seg)<10:
            #game_is_on = False
            score.game_over()
            score.reset()
            snake.reset()

screen.exitonclick()
