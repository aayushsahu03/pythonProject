from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface
import os

# absolute_path = os.path.dirname(__file__)
# print(absolute_path)
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)


# The below while has been commented out because it will interfere with Tkinter
# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
