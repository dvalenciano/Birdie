from datetime import datetime
from models.db import db


class Location(db.Model):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(255), nullable=False, unique=False)
    note = db.Column(db.String(255), nullable=False, unique=False)
    bird_type = db.Column(db.String(255), nullable=False, unique=False)
    created_at = db.Column(db.DateTime, default=str(
        datetime.utcnow()), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(
    ), nullable=False, onupdate=datetime.now())

    def __init__(self, location, note, bird_type):
        self.location = location
        self.note = note
        self.bird_type = bird_type

    def json(self):
        return {"id": self.id, "location": self.location, "note": self.note, "bird_type": self.bird_type, "created_at": str(self.created_at), "updated_at": str(self.updated_at)}

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def find_all(cls):
        locations = Location.query.all()
        return [c.json() for c in locations]

    @classmethod
    def find_by_id(cls, location_id):
        location = Location.query.filter_by(id=location_id).first()
        return location
