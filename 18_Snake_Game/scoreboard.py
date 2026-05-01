from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("OCR A EXTENDED", 14, "bold")

class Scoreboard(Turtle):
    """Displays user's score"""
    def __init__(self):
        super().__init__()
        self.score = 0
        
        try:
            with open("data.txt", mode='r') as data:
                self.high_score = int(data.read())
        except FileNotFoundError:
            self.high_score = 0

        self.hideturtle()
        self.penup()
        self.setposition(0, 270)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clears and writes the updated text on screen"""
        self.clear()
        self.write(arg=f"Score: {self.score} - High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        

    def refresh_score(self):
        """Updates current user's score in game"""
        self.score += 1
        self.clear()
        self.update_scoreboard()

    
    def reset(self):
        """Updates high score through current score"""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as data:
                data.write(str(self.high_score))

        self.score = 0
        self.update_scoreboard()