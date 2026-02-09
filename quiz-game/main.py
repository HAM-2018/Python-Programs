from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


questions_left = len(question_bank)
quiz = QuizBrain(question_bank)
while questions_left != 0:

    quiz.next_question()
    questions_left -= 1
quiz.end_game()
