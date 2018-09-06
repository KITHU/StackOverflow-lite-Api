"""create app module the factory way"""
from flask import Flask
from flask_restplus import Api
from flask_restplus import namespace
from flask_restplus import Resource
from app.questions import Questions
from app.questions import QuestionsWithId
from app.questions import Answer
# local import
from instance.config import app_config




def create_app(config_name):
    """create app function"""
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    #app.config.from_pyfile('config.py')
    api = Api(app)

    api.add_resource(Questions, '/api/v1/question')
    api.add_resource(QuestionsWithId, '/api/v1/question/<id>')
    api.add_resource(Answer, '/api/v1/question/<id>/answer')
    return app
