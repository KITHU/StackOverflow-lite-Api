import unittest
from app.models import Models
from app import create_app
from app.questions import Questions,QuestionsWithId,Answer

class TestModels(unittest.TestCase):
    def setUp(self):
        app = create_app('testing')
        self.tester = app.test_client(self)

        self.new_Question = ['data structures',
         'how to copy a python dictionary to another?']

        self.new_question = {"title":"sets",
        "body":"Are set mutable?"}

        self.new_question1 = {"title":" ",
        "body":"Are set mutable?"}

        self.new_question2 = {"title":"lists ",
        "body":" "}

        self.new_answer = {"answer":"my answer is bhhhhhhh"}


    


    def test_add_question(self):
        """Tests if add question method works"""
        qst = Models()
        qst.add_question(self.new_Question[0], self.new_Question[1])
        all_qst = qst.get_all_questions()
        dct = all_qst[0]
        self.assertEqual(dct["title"], self.new_Question[0])

    def test_get_a_question1(self):
        qst = Models()
        all_qst = qst.get_all_questions()
        dct = all_qst[0]
        id = dct["id"]
        question = qst.get_a_question(id)
        self.assertEqual(question["Question"],self.new_Question[1])

    def test_get_a_question(self):
        """Tests if get a question works with wrong id"""
        qst = Models()
        one_question = qst.get_a_question("eb675fkxkdffdg")
        self.assertEqual(one_question, "No question with that id")
    
    def test_answer_a_question(self):
        qst = Models()
        all_qst = qst.get_all_questions()
        dct = all_qst[0]
        id = dct["id"]
        qst.answer_a_question(id, "use dict1 = dict2.copy()")
        ans = qst.get_answers_to_a_question(id)
        self.assertEqual(ans[0],"use dict1 = dict2.copy()")

    def test_api_can_return_all_questions(self):
        res = self.tester.get("/api/v1/question")
        self.assertEqual(res.status_code,200)

    
    def test_api_can_post_a_questions(self):
        res = self.tester.post("/api/v1/question",data=self.new_question)
        self.assertEqual(res.status_code,201)
        self.assertIn('question posted successfully',str(res.data))

        res1 = self.tester.post("/api/v1/question",data=self.new_question1)
        self.assertEqual(res1.status_code,400)

        res2 = self.tester.post("/api/v1/question",data=self.new_question2)
        self.assertEqual(res2.status_code,400)



    def test_api_can_get_a_questions(self):
        res = self.tester.get("/api/v1/question/rt6575766")
        self.assertEqual(res.status_code,400)



    def test_api_post_an_answer(self):
        res = self.tester.post("/api/v1/question/rt6575766/answer",data=self.new_answer)
        self.assertEqual(res.status_code,201)
       


    