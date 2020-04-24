import jwt
import os

from pathlib import Path
from flask_restful import Resource
from flask import request
from datetime import datetime, timedelta
from dotenv import load_dotenv

from app.models import Customer

env_path = Path('.') / '.flaskenv'
load_dotenv(dotenv_path=env_path)


class Login(Resource):  # /auth/login
    def post(self):
        username = request.form['username']

        customer = Customer.get(username=username)

        return {'info': customer.to_dict()}


class Index(Resource):  # /
    def get(self):
        customer = Customer(
            name="Dave",
            last_name="Flr",
            id_card="55588877744",
            passport="9897987",
            direction="Leon Nicaragua",
            phone_number="87459874",
            email="dave@protonmail.com",
            birth_date="10-05-1887",

            # Login credentials
            username="dave",
            password_hash="secret"

        )
        return {'info': customer.to_dict()}


def encode_auth_token(self, user_id):
    """
    Generates the Auth Token
    :return: string
    """
    try:
        payload = {
            'exp': datetime.utcnow() + timedelta(days=0, seconds=200),
            'iat': datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(
            payload,
            os.getenv('SECRET'),
            algorithm='HS256'
        )
    except Exception as e:
        return e
