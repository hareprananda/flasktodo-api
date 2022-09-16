import datetime
from flask import jsonify, request
import validators
from src.database.models.UserModel import UserModel
from src.database.models import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token


def public_endpoint(function):
    function.is_public = True
    return function

class UserController: 
    def register(self):
        name = request.get_json().get('name', '')
        password = request.get_json().get('password', '')
        email = request.get_json().get("email", "")
        if len(password) < 8:
            return jsonify({"status":"error", 'message': 'Password should be at least 8 character'}), 422
        if len(name) < 8:
            return jsonify({"status":"error", 'message': 'Name should be at least 8 character'}), 422

        if not validators.email(email):
            return jsonify({"status":"error", 'message': 'Please provice correct format of email'}), 422 
        
        if UserModel.query.filter_by(email=email).one_or_none() != None:
            return jsonify({"status": "error", "message": "Email used already"}), 422

        pwHash = generate_password_hash(password)
        
        newUser = UserModel(name=name, email=email, password=pwHash)
        db.session.add(newUser)
        db.session.commit()
        return jsonify({'status': "success", 'message': 'Successfully create new user '+repr(newUser)})


        
    
    @public_endpoint
    def login(self):
        email = request.json.get('email', '')
        password = request.json.get('password', '')
        print({
            "email": email,
            "password": password
        })
        print(getattr(request, 'test', 'sing ade nani'))

        user = UserModel.query.filter_by(email=email).first()
        if user: 
            isPassCorrect = check_password_hash(user.password, password)
            if isPassCorrect: 
                refresh = create_refresh_token(identity=user.id)
                access = create_access_token(identity={"id": user.id, "name": user.name}, expires_delta=datetime.timedelta(days=30))
                return jsonify({
                    'status': 'success',
                    'message': '',
                    'data': {
                        'access_token': access,
                        'refresh_token': refresh
                    }
                })
        return jsonify({'status': 'error', 'message': 'User not found'}), 404
                
