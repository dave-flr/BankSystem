from flask_restful import Resource

from app.models import User


class HelloWorld(Resource):
    def get(self):
        user = User(login='carl', password='password')
        return {'user created': user.to_dict()}
