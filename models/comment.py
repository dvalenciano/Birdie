from datetime import datetime
from models.db import db


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=str(
        datetime.utcnow()), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(
    ), nullable=False, onupdate=datetime.now())
    bird_id = db.Column(db.Integer, db.ForeignKey('birds.id'), nullable=False)

    bird = db.relationship("Bird", cascade='all',
                           backref=db.backref('birds', lazy=True))

    def __init__(self, comment, bird_id):
        self.comment = comment
        self.bird_id = bird_id

    def json(self):
        return {"id": self.id, "comment": self.comment, "bird_id": self.bird_id, "created_at": str(self.created_at), "updated_at": str(self.updated_at)}

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def find_all(cls):
        return Comment.query.all()

    @classmethod
    def find_by_id(cls, comment_id):
        comment = Comment.query.filter_by(id=comment_id).first()
        return comment
