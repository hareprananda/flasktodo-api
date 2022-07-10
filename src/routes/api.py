from flask import Blueprint
from src.controller.TodoController import TodoController
from src.controller.StatusController import StatusController
from src.controller.UserController import UserController


app = Blueprint('app', __name__)


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
