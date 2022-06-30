from flask import Blueprint
from src.controller.TodoController import TodoController


app = Blueprint('app', __name__)


app.route('/', methods=['GET'])(TodoController().store)
app.route('/edit', methods=['GET'])(TodoController().edit)