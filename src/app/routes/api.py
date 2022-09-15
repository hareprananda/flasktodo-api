from flask import Blueprint, abort, request, Response, jsonify
from src.app.controller.TodoController import TodoController
from src.app.controller.StatusController import StatusController
from src.app.controller.UserController import UserController
from flask_jwt_extended import verify_jwt_in_request
from flask_jwt_extended.exceptions import NoAuthorizationError
from functools import wraps
from src.app.middleware.TestMiddleware import Middleware

app = Blueprint('app', __name__)


@app.before_request
def auth():    
    path = request.path[:12]
    if path == "/api/v1/auth" :
        return
    try:
        verify_jwt_in_request()
    except NoAuthorizationError as e:
        response = jsonify({'message': 'Unauthorized'})
        response.status_code = 401
        return response
    # print("this should be authorized")




app.route('/status', methods=['GET'])(StatusController().getStatus)
app.route('/status', methods=['POST'])(StatusController().addStatus)
app.route('/status/<int:id>', methods=['DELETE'])(StatusController().delete)
app.route('/status/<int:id>', methods=['PUT'])(StatusController().update)

app.route('/todo', methods=['GET'])(TodoController().getAll)
# app.route('/todo', methods=['POST'])(TodoController().store)
# app.route('/todo/<int:id>', methods=['PUT'])(TodoController().update)
# app.route('/todo/<int:id>', methods=['DELETE'])(TodoController().delete)

app.route('/auth/register', methods=["POST"])(UserController().register)
app.route('/auth/login', methods=["POST"])(UserController().login)
