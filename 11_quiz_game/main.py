from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question1 = Question(question["text"], question["answer"])
    question_bank.append(question1)

quiz_brain1 = QuizBrain(question_bank)

while quiz_brain1.still_has_questions():
    quiz_brain1.next_question()

print(f"You've completed your quiz and you final score is {quiz_brain1.score}/{quiz_brain1.question_number}")
