from models.db import db
from models.location import Location
from flask_restful import Resource
from flask import request
from sqlalchemy.orm import joinedload


class Locations(Resource):
    def get(self):
        location = Location.find_all()
        return location

    def post(self):
        data = request.get_json()
        params = {}
        for c in data.keys():
            params[c] = data[c]
        location = Location(**params)
        location.create()
        return location.json(),  201


class LocationDetail(Resource):
    def get(self, location_id):
        location = Location.query.options(joinedload(
            'bird')).filter_by(id=location_id).first()
        return{**location.json(), "bird": location.user.json()}

    def delete(self, location_id):
        location = Location.find_by_id()
        if not location:
            return {"msg": "Not found"}, 404
        db.session.delete(location)
        db.session.commit()
        return {"msg": "Comment Deleted", "payload": location_id}
