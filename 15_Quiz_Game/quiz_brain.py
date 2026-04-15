
class QuizBrain:
    """Manages the logic and state of the quiz."""
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        """Checks if the program still has questions to ask"""
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        """Displays current question and shows it on screen (also verifies only valid entries)."""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ").capitalize()

        while user_answer not in ['True','False']:
            print("Please only type True or False!")
            user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ").capitalize()
            continue

        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """Reviews if the user answer and the database answer are the same or not"""
        if user_answer == correct_answer.capitalize():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")