from models.db import db
from models.bird import Bird
from models.user import User
from flask_restful import Resource
from flask import request
from sqlalchemy.orm import joinedload


class Birds(Resource):
    def get(self):
        birds = Bird.find_all()
        return birds

    def post(self):
        data = request.get_json()
        params = {}
        for k in data.keys():
            params[k] = data[k]
        bird = Bird(**params)
        bird.create()
        return bird.json(),  201


class BirdDetail(Resource):
    def get(self, bird_id):
        bird = Bird.query.options(joinedload(
            'bird')).filter_by(id=bird_id).first()
        return{**bird.json(), "user": bird.user.json()}

    def put(self, bird_id):
        data = request.get_json()
        bird = Bird.find_by_id(bird_id)
        for k in data.keys():
            bird[k] = data[k]
        db.session.commit()
        return bird.json()

    def delete(self, bird_id):
        bird = Bird.find_by_id()
        if not bird:
            return {"msg": "Not found"}, 404
        db.session.delete(bird)
        db.session.commit()
        return {"msg": "Bird Deleted", "payload": bird_id}
