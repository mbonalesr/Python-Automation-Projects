import os
os.system('cls')

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

logo = """
                                                                                       
   _|_|                _|                  _|_|_|                                      
 _|    _|    _|    _|      _|_|_|_|      _|          _|_|_|  _|_|_|  _|_|      _|_|    
 _|  _|_|    _|    _|  _|      _|        _|  _|_|  _|    _|  _|    _|    _|  _|_|_|_|  
 _|    _|    _|    _|  _|    _|          _|    _|  _|    _|  _|    _|    _|  _|        
   _|_|  _|    _|_|_|  _|  _|_|_|_|        _|_|_|    _|_|_|  _|    _|    _|    _|_|_|  
                                                                                       
                                                                                       
"""

for question in question_data:
    new_q = Question(question['question'], question['correct_answer'])
    # print(f"Question: {question['text']}\nAnswer: {question['answer']}")
    question_bank.append(new_q)

# print(question_bank)
# print(question_bank[0].text)

test = QuizBrain(question_bank)

while test.still_has_questions():
    print(logo)
    test.next_question()

print(f"You've completed the quiz\nYour final score is: {test.score}/{test.question_number}")