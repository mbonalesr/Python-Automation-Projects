import html

class QuizBrain:
    """Manages the logic and state of the quiz."""
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        """Checks if the program still has questions to ask"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Displays current question and shows it on screen (also verifies only valid entries)."""
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        
        return f"Q.{self.question_number}: {q_text} (True/False): "

    def check_answer(self, user_answer):
        """Reviews if the user answer and the database answer are the same or not"""
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
        
