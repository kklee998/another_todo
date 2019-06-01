from flask import request
from flask_restful import Resource
from models import db
from models.ToDoModel import ToDoSchema, ToDo

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
            user=data['user'],
            isdone=False
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


class ToDoUpdate(Resource):
    def put(self, todo_id):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400

        data, errors = todo_schema.load(json_data)
        if errors:
            return {"status": "error", "data": errors}, 422

        ToDo.query.filter(ToDo.todo_id == todo_id).update({
            "isdone": data['isdone'],
            "todo": data['todo']
        })

        db.session.commit()

        return {'status': "succuss", 'data': 'Todo updated successfully'}

    def delete(self, todo_id):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400

        data, errors = todo_schema.load(json_data)
        if errors:
            return {"status": "error", "data": errors}, 422

        ToDo.query.filter(ToDo.todo_id == todo_id).delete()
        db.session.commit()

        return {"status": 'success', 'data': "Deleted"}, 200
