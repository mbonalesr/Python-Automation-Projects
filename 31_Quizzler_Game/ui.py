from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    """Creates and manages the graphical user interface (GUI) for the trivia game"""
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Mau's Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.canvas = Canvas(height=250, width=300, highlightthickness=0, bg="white")
        self.question_label = self.canvas.create_text(
            150, 
            125,
            width=280, 
            text="Question label", 
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)

        self.false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        self.score_label = Label(text="Score: 0", font=("Arial", 10, "normal"), fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """Retrieves the next question from the quiz brain and displays it on the UI"""
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_label, text=q_text)
        else:
            self.canvas.itemconfig(self.question_label, text="You've reached the end of the game")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        """Checks if the user's answer (True) is correct"""
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        """Checks if the user's answer (False) is correct"""
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        """Flashes the canvas green or red based on the answer, then loads the next question"""
        if is_right == True:
            self.canvas.config(bg="green")
            self.window.after(1000, func=self.get_next_question)
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, func=self.get_next_question)