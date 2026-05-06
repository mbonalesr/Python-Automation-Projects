from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Mau's Pong Game")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreb = Scoreboard()

screen.listen()
screen.onkey(key="w", fun=left_paddle.go_up)
screen.onkey(key="Up", fun=right_paddle.go_up)
screen.onkey(key="s", fun=left_paddle.go_down)
screen.onkey(key="Down", fun=right_paddle.go_down)

game_on = True
while game_on:
    time.sleep(ball.movement_speed)
    screen.update()
    ball.move_and_bounce_y()
    
    #Detect collision with both paddles
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
        ball.movement_speed *= 0.9

    #Detect when paddle misses
    if ball.xcor() > 380: #Right paddle misses
        ball.reset_position()
        scoreb.left_point()
    elif ball.xcor() < -380: #Left paddle misses
        ball.reset_position()
        scoreb.right_point()
