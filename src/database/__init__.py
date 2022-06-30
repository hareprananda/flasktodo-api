from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import DeclarativeMeta
from datetime import datetime


db = SQLAlchemy()

BaseModel:DeclarativeMeta = db.Model


class Users(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    todos = db.relationship('Todo', backref='user')

    def __repr__(self):
        return '<Name %r>' % self.name

class Todo(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(200))
    creator = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Name %r>' % self.todo

