import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    """A simple attempt to represent cars in game"""
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """Produces a single car"""
        if random.randint(1,6) == 3: #random chance of generating car and avoid car's overpopulation
            car = Turtle("square")
            car.color(random.choice(COLORS))
            car.shapesize(1,2)
            car.penup()

            random_y = random.randint(-250, 250)
            car.setposition(300, random_y)
            self.all_cars.append(car)


    def move_cars(self):
        """Make the cars to advance"""
        for car in self.all_cars:
            car.backward(self.car_speed)

    def more_speed(self):
        """Adds more speed to the cars when player crosses road"""
        self.car_speed += MOVE_INCREMENT
