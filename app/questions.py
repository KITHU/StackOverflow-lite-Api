from flask_restplus import Resource


class Questions(Resource):
    def post():
        return{"hello":"james post"}