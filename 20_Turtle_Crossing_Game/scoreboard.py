from turtle import Turtle

FONT = ("Courier", 26, "bold")


class Scoreboard(Turtle):
    """Displays level of the game and if the game is over"""
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.setposition(-205, 250)
        self.write(arg=f"Level: {self.level}", align='center', font=FONT)

    def update_level(self):
        """Shows current score based on game's points"""
        self.clear()
        self.level += 1
        self.write(arg=f"Level: {self.level}", align='center', font=FONT)

    def game_over(self):
        """Display an end of the game message"""
        self.setposition(0, 0)
        self.write("GAME OVER", align='center', font=("Courier", 16, "bold"))
    