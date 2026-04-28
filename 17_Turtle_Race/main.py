import os, random
os.system('cls')
from turtle import Turtle, Screen

is_race_on = False

screen = Screen()
screen.setup(width=600, height=500)

user_bet = screen.textinput(title="Make your bet", prompt="Which turle will win the race? Enter a color: ").lower()
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'gray']

y_position = -200
all_turtles = []
 
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-270, y=y_position)
    y_position += 50
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 280: #check if a turtle crossed the finish line
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()
