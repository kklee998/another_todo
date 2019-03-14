from flask import Blueprint
from flask_restful import Api
from resources.Hello import Hello
from resources.ToDo import ToDoResource, ToDoFilter
from resources.User import Register, Login

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(Hello, '/hello')
api.add_resource(ToDoResource, '/todos')
api.add_resource(ToDoFilter, '/todos/<user>')
api.add_resource(Register, '/register')
api.add_resource(Login, '/login')
