from . import db, ma
from marshmallow import fields, validate


class ToDo(db.Model):
    __tablename__ = 'todos'
    todo_id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(250), nullable=False)
    user = db.Column(db.String(250), nullable=False)
    isdone = db.Column(db.Boolean, default=False)
    creation_date = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    def __init__(self, todo, user, isdone):
        self.todo = todo
        self.user = user
        self.isdone = isdone


class ToDoSchema(ma.Schema):
    todo_id = fields.Integer(dump_only=True)
    todo = fields.String(required=True, validate=validate.Length(1))
    user = fields.String(required=True, validate=validate.Length(1))
    isdone = fields.Boolean()
    creation_date = fields.DateTime()
