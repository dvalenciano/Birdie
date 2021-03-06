from models.db import db
from models.bird import Bird
from flask_restful import Resource
from flask import request
from sqlalchemy.orm import joinedload


class Birds(Resource):
    def get(self):
        birds = Bird.find_all()
        return birds

    def post(self):
        data = request.get_json()
        print(data)
        params = {}
        for k in data.keys():
            params[k] = data[k]
        bird = Bird(**params)
        bird.create()
        return bird.json(),  201


class BirdDetail(Resource):
    def get(self, bird_id):
        bird = Bird.find_by_id(bird_id)
        return{**bird.json()}

    def put(self, bird_id):
        data = request.get_json()
        bird = Bird.find_by_id(bird_id)
        for d in data.keys():
            setattr(bird, d, data[d])
        db.session.commit()
        return bird.json()

    def delete(self, bird_id):
        bird = Bird.find_by_id(bird_id)
        if not bird:
            return {"msg": "Not found"}, 404
        db.session.delete(bird)
        db.session.commit()
        return {"msg": "Bird Deleted", "payload": bird_id}
