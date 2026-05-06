from turtle import Turtle

class Paddle(Turtle):
    """Emulates a tennis paddle for Pong Game"""
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.setposition(position)

    def go_up(self):
        """Moves the paddle upwards"""
        new_y = self.ycor() + 20
        self.setposition(self.xcor(), new_y)


    def go_down(self):
        """Moves the paddle downwards"""
        new_y = self.ycor() - 20
        self.setposition(self.xcor(), new_y)
