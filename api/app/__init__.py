from flask import Flask
from flask_restful import Api
from pony.flask import Pony

from config import config
from .models import *
from .views import *

server = Flask(__name__)
server.config.update(config)

Pony(server)

api = Api(server)

api.add_resource(HelloWorld, '/')
