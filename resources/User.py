from flask import request
from flask_restful import Resource
from Model import db, User, UserSchema

users_schema = UserSchema(many=True)
user_schema = UserSchema()


class Register(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return{'message': 'No input data provided'}, 400

        data, errors = user_schema.load(json_data)
        if errors:
            return {"status": "error", "data": errors}, 422

        user = User(
            username=data['username'],
            password=data['password']
        )
        db.session.add(user)
        db.session.commit()

        result = user_schema.dump(user).data

        return {'status': "success", 'data': result}, 201


class Login(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return{'message': 'No input data provided'}, 400

        data, errors = user_schema.load(json_data)
        if errors:
            return {"status": "error", "data": errors}, 422

        username = data['username']
        password = data['password']

        data = User.query.filter_by(
            username=username, password=password).first()

        if data is not None:
            return {"status": "success"}, 200

        return {
            'status': "error", 'data': "Password or Username is invalid"
        }, 401
