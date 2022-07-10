from flask import jsonify, request
from src.database.models import db
from src.database.models.StatusModel import StatusModel

class StatusController:
    def getStatus(self):
        statusDatas = StatusModel.query.all()
        for index, statusData in enumerate(statusDatas):
            statusDatas[index] = statusData.as_dict()
        return jsonify({'data': statusDatas})
    
    def addStatus(self):
        name = request.get_json().get('name', '')
        newStatus = StatusModel(name=name)
        db.session.add(newStatus)
        db.session.commit()
        return jsonify({'status': 'succes', 'data': newStatus.as_dict()})
    
    def delete(self, id):
        findStatus = StatusModel.query.get(id)
        if findStatus :
            db.session.delete(findStatus)
            db.session.commit()
            return jsonify({'status': 'success', 'message': 'delete '+repr(findStatus)+' success'})

        return jsonify({'status': 'Success', 'message': 'Not found'}), 404
    
    def update(self, id):
        findStatus = StatusModel.query.get(id)
        if bool(findStatus) is False :
            return jsonify({'status': 'Not found'}), 404
        newName = request.get_json().get('name', '')
        findStatus.name = newName
        db.session.commit()
        return jsonify({'status':'Success', 'data': findStatus.as_dict()})


       
    

