from models.db import db
from models.comment import Comment
from flask_restful import Resource
from flask import request


class Comments(Resource):
    def get(self):
        comment = Comment.find_all()
        return comment

    def post(self):
        data = request.get_json()
        params = {}
        for c in data.keys():
            params[c] = data[c]
        comment = Comment(**params)
        comment.create()
        return comment.json(),  201


class CommentDetail(Resource):
    def get(self, comment_id):
        comment = Comment.find_by_id(comment_id)
        return{**comment.json()}

    def delete(self, comment_id):
        comment = Comment.find_by_id()
        if not comment:
            return {"msg": "Not found"}, 404
        db.session.delete(comment)
        db.session.commit()
        return {"msg": "Comment Deleted", "payload": comment_id}
