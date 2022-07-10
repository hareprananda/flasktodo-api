from src.database.models import db

class StatusModel(db.Model):
    __tablename__= 'status'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    def __repr__(self) -> str:
        return 'Status >>> ' + self.name