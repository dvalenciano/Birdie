from flask import request
from flask_restful import Resource
from models.user import User
from models.db import db
from sqlalchemy.orm import joinedload


class Users(Resource):
    def get(self):
        users = User.find_all()
        return [u.json() for u in users]

    def post(self):
        data = request.get_json()
        user = User(**data)
        user.create()
        return user.json(), 201


class UserDetail(Resource):
    def get(self, user_id):
        user = User.query.options(joinedload(
            'tasks')).filter_by(id=user_id).first()
        print(user.task)
        tasks = [t.json() for t in user.tasks]
        return {**user.json(), "tasks": tasks}

    def put(self, user_id):
        data = request.get_json()
        user = User.find_by_id(user_id)
        for k in data.keys():
            setattr(user, k, data[k])
        db.session.commit()
        return user.json()

    def delete(self, user_id):
        user = User.find_by_id(user_id)
        if not user:
            return {"msg": "user not found"}, 404
        db.session.delete(user)
        db.session.commit()
        return {"msg": "User Deleted", "payload": user_id}
