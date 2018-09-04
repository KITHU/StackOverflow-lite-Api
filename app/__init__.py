from flask import Flask
from flask_restplus import Api,namespace
from flask_restplus import model
from flask_restplus import fields
from flask_restplus import Resource
from flask_restplus import reqparse

from app.questions import Questions

# local import
from instance.config import app_config




def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    #app.config.from_pyfile('config.py')
    api = Api(app)

    api.add_resource(Questions, '/api/v1/question')
    
    
   
    return app
