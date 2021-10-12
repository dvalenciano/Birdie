from models.db import db
from models.comment import Comment
from models.user import User
from flask_restful import Resource
from flask import request
from sqlalchemy.orm import joinedload


class Comments(Resource):
    def get(self):
        comment = Comment.find_all()
        return comment

    def post(self):
        data = request.get_json()
        params = {}
        for k in data.keys():
            params[k] = data[k]
        comment = Comment(**params)
        comment.create()
        return comment.json(),  201


class CommentDetail(Resource):
    def get(self, comment_id):
        comment = Comment.query.options(joinedload(
            'bird')).filter_by(id=comment_id).first()
        return{**comment.json(), "bird": comment.user.json()}

    def delete(self, comment_id):
        comment = Comment.find_by_id()
        if not comment:
            return {"msg": "Not found"}, 404
        db.session.delete(comment)
        db.session.commit()
        return {"msg": "Comment Deleted", "payload": comment_id}
