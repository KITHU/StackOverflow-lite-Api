from flask_restplus import Namespace
from flask_restplus import fields
from flask_restplus import Resource


api = Namespace('auth', description='user related functionalities')

class Signup(Resource):
    def post(self):
        return{"message": "Account created"}, 201



class Login(Resource):
    def post(self):
        return{"message":"loged in"}, 200
       
