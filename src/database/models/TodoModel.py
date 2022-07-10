from src.database.models import db

class TodoModel(db.Model):
    __tablename__="todo"
    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Integer, db.ForeignKey('status.id'), nullable=False)
    user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)