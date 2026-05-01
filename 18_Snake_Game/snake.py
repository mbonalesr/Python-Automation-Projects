from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """A simple attempt to emulate a snake"""

    def __init__(self):
        """Initializing variables"""
        self.initial_positions = [(0,0), (-20,0), (-40,0)]
        self.segments = []
        self.generate_snake()
        self.head = self.segments[0]


    def generate_snake(self):
        """Creates initial squares of the snake"""
        for position in self.initial_positions:
            self.add_segment(position)


    def extend(self):
        """Stretches along the length of the snake"""
        self.add_segment(self.segments[-1].position())

    def reset(self):
        """Initialize the snake again"""
        for seg in self.segments:
            seg.setposition(1000,1000)
        self.segments.clear()
        self.generate_snake()
        self.head = self.segments[0]

    def add_segment(self, position):
        """Attaches a square or segment into the snake"""
        square = Turtle(shape="square")
        square.color("white")
        square.penup()
        square.setposition(position)
        self.segments.append(square)


    def movement(self):
        """Makes the snake advance"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(20)


    def go_up(self):
        """Snake moves upwards"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def go_left(self):
        """Snake moves to his left side"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def go_down(self):
        """Snake moves downwards"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def go_right(self):
        """Snake moves to his right side"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
