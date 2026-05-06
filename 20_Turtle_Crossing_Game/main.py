import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Mau's Turtle Crossing Game")
screen.tracer(0)

turtle = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=turtle.go_up)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_cars()


    #Detecting collision with a car
    for car in cars.all_cars:
        if turtle.distance(car) < 20:
            score.game_over()
            game_is_on = False

    #Detecting when player has reached the other side
    if turtle.is_at_finish_line():
        turtle.return_to_start()
        cars.more_speed()
        score.update_level()

screen.exitonclick()
