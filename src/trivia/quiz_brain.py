class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score : int = 0
        self.question_list = q_list
        self.current_question = None
        self.answereds : int = 0

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)

    def next_question(self) -> str:
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        return f"Q.{self.question_number}: {self.current_question.text}"

    def check_answer(self, user_answer) -> bool:
        self.answereds +=1
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
            return True
        else:
            print("That's wrong.")
            return False