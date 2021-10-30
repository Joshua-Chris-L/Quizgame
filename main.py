from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    q_text = question["text"]
    q_answer = question["answer"]
    new_Question = Question(q_text, q_answer)
    question_bank.append(new_Question)

#QuizBrain(question_bank)
quiz = QuizBrain(question_bank)

cont = True
while cont:
    if len(question_bank) <=12:
        quiz.next_question()
    else:
        cont = False

print("You've completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.number}")


