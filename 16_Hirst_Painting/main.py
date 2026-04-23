import colorgram, random
import turtle as t
from turtle import Screen

t.colormode(255)

color_list = [(203, 172, 108), (222, 228, 235), (153, 180, 196), (193, 161, 177), (152, 186, 174), (214, 204, 113), (207, 179, 198), (175, 189, 213), (160, 213, 187), (161, 203, 215), (113, 122, 185), (187, 162, 62), (215, 180, 180), (198, 206, 46), (105, 113, 147)]

t.penup()
y_position = -200
t.speed(8)

for _ in range(10):
    t.setposition(-200, y_position)
    for _ in range(10):
        t.dot(20, random.choice(color_list))
        t.hideturtle()
        t.forward(50)
    y_position += 50

Screen().exitonclick()
