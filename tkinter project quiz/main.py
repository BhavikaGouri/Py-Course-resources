from question_model import Question
from quiz_brain import QuizBrain
import requests
from ui import UserInterface

parameters = {
    "amount": 10,
    "type": "boolean"
}

question_bank = []
response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean", params=parameters)
questions = response.json()
question_data = questions["results"]

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
obj = UserInterface(quiz)
