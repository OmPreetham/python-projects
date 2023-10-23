from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    new_ques = Question(question["text"], question["answer"])
    question_bank.append(new_ques)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()


print("You've completed the Quizzes")
print(f"Your final score {quiz.score}/{len(question_bank)}")