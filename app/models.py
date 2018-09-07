"""models module"""
import datetime
import uuid


class Models():
    """class to store data about the question"""
    database = {
        "my_questions": [],
        "my_answers": []
    }

    def __init__(self):
        """init method for class Model"""
        self.date = str(datetime.datetime.now().date())

    def get_all_questions(self):
        """method to fetch all questions available"""
        all_questions = []
        all_questions = self.database["my_questions"]
        return all_questions

    def add_question(self, question_title, question_body):
        """method to add a question to database"""
        self.id = uuid.uuid4().hex
        qst = {"id": self.id,
               "title": question_title,
               "Question": question_body,
               "date": self.date}
        self.database["my_questions"].append(qst)

    def get_a_question(self, id):
        """method to fetch a question by id"""

        qstion = {}
        for question in self.database["my_questions"]:
            if id in question.values():
                ans = self.get_answers_to_a_question(id)
                qstion = question.copy()
                qstion["answers"] = ans
                return qstion
        return "No question with that id"

    def answer_a_question(self, question_id, answer):
        """method to add an answer to a question"""

        ans = {"question_id": question_id, "answer": answer}
        self.database["my_answers"].append(ans)

    def get_answers_to_a_question(self, id):  # pylint:C0103
        """method to fetch answers available to a question"""

        ans = []
        for answers in self.database["my_answers"]:
            if id in answers.values():
                ans.append(answers['answer'])
        return ans
    