from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    """Emulate a player/turtle behavior"""
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setposition(STARTING_POSITION)
        self.setheading(90)

    def go_up(self):
        """Move the player upwards"""
        self.forward(MOVE_DISTANCE)


    def is_at_finish_line(self):
        """Verify if player has passed all cars"""
        return self.ycor() > FINISH_LINE_Y
        
    def return_to_start(self):
        """Take the player back to the beginning"""
        self.setposition(STARTING_POSITION)
    