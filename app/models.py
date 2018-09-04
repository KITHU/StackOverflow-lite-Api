import datetime
import uuid

class Models(object):
    database = {
        "my_questions":[],
        "my_answers":[]
    }
    def __init__(self):
        
        self.date = str(datetime.datetime.now().date())

    def get_all_questions(self):
        all_questions=[]
        all_questions = self.database["my_questions"]
        return all_questions

    def add_question(self,question_title,question_body):
        self.id = uuid.uuid4().hex
        qst = {"id":self.id,"title":question_title,"Question":question_body,"date":self.date}
        self.database["my_questions"].append(qst)
       
    
    def get_a_question(self,id):
        qstion = {}
        for question in self.database["my_questions"]:
            if (id in question.values()) == True:
                ans = self.get_answers_to_a_question(id)
                qstion = question.copy()
                qstion["answers"] = ans
                return qstion
        return "No question with that id"

    def answer_a_question(self,question_id,answer):
        ans = {"question_id":question_id,"answer":answer}
        self.database["my_answers"].append(ans)

    def get_answers_to_a_question(self,id):
        ans = []
        for answers in self.database["my_answers"]:
            if (id in answers.values()) == True:
                ans.append(answers['answer']) 
        return ans



        