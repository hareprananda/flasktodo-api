from flask import jsonify
from src.database.models.UserModel import UserModel
from src.database.models.TodoModel import TodoModel
from src.database.models import db

class TodoController:
    def store(self):
        return jsonify({'test': 'Ini berhasil boss'}), 200

    def update(self, id:int):
        mantap = id
        return jsonify({"manusia": "percobaan"})
    
    def getAll(self):
        rawData = db.session.query(TodoModel, UserModel).join(UserModel).all()
        finalData = []
        print(rawData)
        for todo, user in rawData:
            finalData.append({
                "todoName": todo.name,
                "name": user.name,
                "email": user.email
            })
        return jsonify({"status": "success", "data": finalData})
    
    def delete(self, id:int):
        pass 


