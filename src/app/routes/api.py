from flask import Blueprint, abort, request, Response, jsonify
from src.app.controller.TodoController import TodoController
from src.app.controller.StatusController import StatusController
from src.app.controller.UserController import UserController
from flask_jwt_extended import verify_jwt_in_request, decode_token
from flask_jwt_extended.exceptions import NoAuthorizationError

app = Blueprint('app', __name__)


@app.before_request
def auth():    
    path = request.path[:12]
    if path == "/api/v1/auth" :
        return
    try:
        authorization = request.headers.get('Authorization','')[7:]
        verify_jwt_in_request()
        request.auth = decode_token(authorization)["sub"]
    except NoAuthorizationError as e:
        response = jsonify({'message': 'Unauthorized'})
        response.status_code = 401
        return response




app.route('/status', methods=['GET'])(StatusController().getStatus)
app.route('/status', methods=['POST'])(StatusController().addStatus)
app.route('/status/<int:id>', methods=['DELETE'])(StatusController().delete)
app.route('/status/<int:id>', methods=['PUT'])(StatusController().update)

app.route('/todo', methods=['GET'])(TodoController().getAll)
app.route('/todo', methods=['POST'])(TodoController().store)
app.route('/todo/<int:id>', methods=['PUT'])(TodoController().updateTodo)
app.route('/todo/<int:id>', methods=['DELETE'])(TodoController().deleteTodo)

app.route('/auth/register', methods=["POST"])(UserController().register)
app.route('/auth/login', methods=["POST"])(UserController().login)
