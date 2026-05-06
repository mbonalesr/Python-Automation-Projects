from turtle import Turtle

class Scoreboard(Turtle):
    """Displays user's score"""
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0

    def update_score(self):
        """Shows current score based on game's points"""
        self.clear()
        self.setposition(-100, 220)
        self.write(self.left_score, align="center", font=("OCR A EXTENDED", 50, "normal"))
        self.setposition(100, 220)
        self.write(self.right_score, align="center", font=("OCR A EXTENDED", 50, "normal"))

    def left_point(self):
        """Refresh and adds a point to left player"""
        self.left_score += 1
        self.update_score()

    def right_point(self):
        """Refresh and adds a point to right player"""
        self.right_score += 1
        self.update_score()
