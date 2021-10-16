from datetime import datetime
from models.db import db


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255), nullable=False, unique=True)
    bird_type = db.Column(db.String(255), nullable=False, unique=False)
    created_at = db.Column(db.DateTime, default=str(
        datetime.utcnow()), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(
    ), nullable=False, onupdate=datetime.now())

    def __init__(self, comment, bird_type):
        self.comment = comment
        self.bird_type = bird_type

    def json(self):
        return {"id": self.id, "comment": self.comment, "bird_type": self.bird_type, "created_at": str(self.created_at), "updated_at": str(self.updated_at)}

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def find_all(cls):
        comments = Comment.query.all()
        return [c.json() for c in comments]

    @classmethod
    def find_by_id(cls, comment_id):
        comment = Comment.query.filter_by(id=comment_id).first()
        return comment
