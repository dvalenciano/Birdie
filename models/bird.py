from datetime import datetime
from models.db import db


class Bird(db.Model):
    __tablename__ = 'birds'

    id = db.Column(db.Integer, primary_key=True)
    bird_type = db.Column(db.String(255), nullable=False, unique=False)
    color = db.Column(db.String(255), nullable=False, unique=False)
    created_at = db.Column(db.DateTime, default=str(
        datetime.utcnow()), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(
    ), nullable=False, onupdate=datetime.now())

    def __init__(self, bird_type, color):
        self.bird_type = bird_type
        self.color = color

    def json(self):
        return {"id": self.id, "bird_type": self.bird_type, "color": self.color, "created_at": str(self.created_at), "updated_at": str(self.updated_at)}

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def find_all(cls):
        birds = Bird.query.all()
        return [b.json() for b in birds]

    @classmethod
    def find_by_id(cls, bird_id):
        bird = Bird.query.filter_by(id=bird_id).first()
        return bird
