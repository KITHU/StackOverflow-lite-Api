"""this module has routes for questions and answers"""

from flask_restplus import Resource
from flask_restplus import reqparse
from app.models import Models
from utils.validator import Validate as validate


class Questions(Resource):
    """class for question routes"""

    def __init__(self, url):
        """init method for Question class"""
        self.model = Models()
        self.postquestion_arg = reqparse.RequestParser()
        self.postquestion_arg.add_argument('title',
                                           type=str, required=True,
                                           help='title is required!')
        self.postquestion_arg.add_argument('body',
                                           type=str, required=True,
                                           help="body is required")

    def post(self):
        """post a question"""
        valid = validate()
        use_question = self.postquestion_arg.parse_args()
        title = use_question['title']
        if valid.valid_username(title) == False:
            return {"error" : "invalid title"}, 400
        body = use_question['body']
        if valid.valid_username(body) == False:
            return {"error" : "body of your question is invalid"}, 400
        available_q = self.model.get_all_questions()
        for q in available_q:
            if q["Question"] == body:
                return {"error" : "Question already available"}, 400
        self.model.add_question(title, body)
        return{"message" : "question posted successfully"}, 201


    def get(self):
        """get a question http method"""
        all_questions = self.model.get_all_questions()
        if len(all_questions) < 1:
            return {"message": "No questions Available"}, 404
        return {"questions" : all_questions}, 200


class QuestionsWithId(Resource):
    """class to hold question with id"""
    def __init__(self, url):
        self.model = Models()

    def get(self, id):
        """route to get question by id"""
        question = self.model.get_a_question(id)
        if question == "No question with that id":
            return {"message":"No question with that id"}, 400

        return {"Question":question}, 200

class Answer(Resource):
    """Answer class for answers"""
    def __init__(self, url):
        """init for Answers class """
        self.model = Models()
        self.answer_arg = reqparse.RequestParser()
        self.answer_arg.add_argument('answer',
                                     type=str, required=True,
                                     help='answer is required!{"answer":"you ans here"}')

    def post(self, id):
        """route to post an answer"""
        valid = validate()
        user_ans = self.answer_arg.parse_args()
        ans = user_ans['answer']
        if valid.valid_username(ans) == False:
            return {"error":"answer should contain text"}, 400
        question = self.model.get_a_question(id)
        if question == "No question with that id":
            return {"message":"check id and try again"}, 400
        answers = self.model.get_answers_to_a_question(id)
        if ans in answers:
            return{"message":"similar answer alread available"}, 400
        self.model.answer_a_question(id, ans)
        return {"message" : "your answer has been posted"}, 201
    