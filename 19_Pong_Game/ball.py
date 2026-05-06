from turtle import Turtle

class Ball(Turtle):
    """Emulates a ball for Pong Game"""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setposition(0,0)
        self.x_move = 10
        self.y_move = 10
        self.movement_speed = 0.1

    def move_and_bounce_y(self):
        """Moves the ball diagonally across the screen"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.setposition(new_x, new_y)

        if self.ycor() > 280 or self.ycor() < -280:
            self.y_move *= -1

    
    def bounce_x(self):
        """Bump through opposite X axis"""
        self.x_move *= -1

    
    def reset_position(self):
        """
        Returns the ball to the center of the screen and starts moving towards the other player
        """
        self.setposition(0,0)
        self.x_move *= -1
        self.movement_speed = 0.1
