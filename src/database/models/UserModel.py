from src.database.models import db
from datetime import datetime

class UserModel(db.Model):
    __tablename__= 'user'
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(100), unique=True, nullable=False)
    email= db.Column(db.String(30), unique=True, nullable=False)
    password= db.Column(db.String(200), nullable=False)
    created_at= db.Column(db.DateTime, default=datetime.now())

    def __repr__(self) -> str:
        return 'User>>>' + self.name
    