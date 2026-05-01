from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Mau's Snake Game")
screen.tracer(0)

my_snake = Snake()
my_food = Food()
my_scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=my_snake.go_up)
screen.onkey(key="Left", fun=my_snake.go_left)
screen.onkey(key="Down", fun=my_snake.go_down)
screen.onkey(key="Right", fun=my_snake.go_right)


game_is_on = True
while game_is_on:
    screen.update() 
    time.sleep(0.1)
    my_snake.movement()

    #Detecting collision with food
    if my_snake.head.distance(my_food) < 13:
        my_food.refresh()
        my_snake.extend()
        my_scoreboard.refresh_score()

    #Detecting collision with wall
    if my_snake.head.xcor() > 290 or my_snake.head.xcor() < - 290 or my_snake.head.ycor() > 290 or my_snake.head.ycor() < - 290:
        my_scoreboard.reset()
        my_snake.reset()
        

    #Detecting collision with tail
    for segment in my_snake.segments[1:]:
        if my_snake.head.distance(segment) < 10:
            my_scoreboard.reset()
            my_snake.reset()


screen.exitonclick()
