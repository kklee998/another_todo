from flask import request
from flask_restful import Resource
from Model import db, ToDo, ToDoSchema

todos_schema = ToDoSchema(many=True)
todo_schema = ToDoSchema()


class ToDoResource(Resource):
    def get(self):
        todo = ToDo.query.all()
        todo = todos_schema.dump(todo).data
        return {"status": "success", "data": todo}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = todo_schema.load(json_data)
        if errors:
            return {"status": "error", "data": errors}, 422
        todo = ToDo(
            todo=data['todo'],
            user=data['user']
        )
        db.session.add(todo)
        db.session.commit()

        result = todo_schema.dump(todo).data

        return {'status': "success", 'data': result}, 201


class ToDoFilter(Resource):
    def get(self, user):
        todo = ToDo.query.filter(ToDo.user == user)
        todo = todos_schema.dump(todo).data
        return {"status": "success", "data": todo}, 200
