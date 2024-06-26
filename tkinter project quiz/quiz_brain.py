import html


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 1
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        print(self.question_number)
        return self.question_number <= len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number-1]
        q_text = html.unescape(self.current_question.text)
        user_answer = f"Q.{self.question_number}: {q_text}"
        self.question_number += 1
        return user_answer

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            return True
        else:
            return False
