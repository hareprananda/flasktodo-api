from flask import jsonify, request
from src.database.models.UserModel import UserModel
from src.database.models.TodoModel import TodoModel
from src.database.models.StatusModel import StatusModel
from flask_jwt_extended import jwt_required
from src.database.models import db

class TodoController:
    def store(self):
        body = request.get_json()
        newData = {
            "name": body.get('name', ''),
            "status": body.get('status', ''),
            'user': request.auth["id"]
        }
        if '' in list(newData.values()):
            return jsonify({'message': 'Some property missing'}), 400
        findStatus = StatusModel.query.filter_by(id=newData["status"]).first()
        if findStatus == None: 
            return jsonify({'message': 'Wrong Status'}), 400
        newTodo = TodoModel(name=newData["name"], status=newData["status"], user=newData["user"])
        db.session.add(newTodo)
        db.session.commit()        
        return jsonify({'message': 'Success'}), 200

    def updateTodo(self, id:int):
        body = request.get_json()
        updatedData = {
            "name": body.get('name', ''),
            "status": body.get('status', ''),
            'user': request.auth["id"]
        }
        find = TodoModel.query.filter_by(id=id, user=request.auth["id"]).first()
        findStatus = StatusModel.query.filter_by(id= updatedData['status']).first()
        if find == None or findStatus == None or '' in list(updatedData.values()):
            return jsonify({'message': 'Wrong id / provide wrong value'}), 400
        find.status = updatedData['status']
        find.name = updatedData['name']
        db.session.commit()
        return jsonify({'message': 'Update data success'})
    
    def getAll(self):
        rawData = db.session.query(TodoModel, UserModel, StatusModel).join(UserModel).join(StatusModel).all()
        finalData = []
        for todo, user, status in rawData:
            finalData.append({
                "id": todo.id,
                "todoName": todo.name,
                "name": user.name,
                "email": user.email,
                "status": status.name
            })
        return jsonify({"message": "success", "data": finalData})
    
    def deleteTodo(self, id:int):
        TodoModel.query.filter_by(id=id).delete()
        db.session.commit()
        return jsonify({"message": "Delete success"})


