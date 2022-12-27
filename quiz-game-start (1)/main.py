from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
if quiz.score == quiz.question_number:
    print("You've completed the quiz! ")
    print("Congratulations!!!! You got all the questions right!")
    print(f"Your final score is: {quiz.score}/{quiz.question_number}")
elif quiz.score > 8:
    print("You've completed the quiz")
    print(f"You've got {quiz.score} right answers! Keep it up!")
elif quiz.score < 5:
    print("You've completed the quiz")
    print(f"You've got {quiz.score} right answers! Better luck next time!")



