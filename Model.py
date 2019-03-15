from marshmallow import fields, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


class ToDo(db.Model):
    __tablename__ = 'todos'
    todo_id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(250), nullable=False)
    user = db.Column(db.String(250), nullable=False)
    isdone = db.Column(db.Boolean, default=False)
    creation_date = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    def __init__(self, todo, user):
        self.todo = todo
        self.user = user


class ToDoSchema(ma.Schema):
    todo_id = fields.Integer(dump_only=True)
    todo = fields.String(required=True, validate=validate.Length(1))
    user = fields.String(required=True, validate=validate.Length(1))
    isdone = fields.Boolean()
    creation_date = fields.DateTime()


class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(250), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)

    def __init__(self, username, password):
        self.user = username
        self.password = password


class UserSchema(ma.Schema):
    user_id = fields.Integer(dump_only=True)
    user = fields.String(required=True, validate=validate.Length(1))
    password = fields.String(required=True, validate=validate.Length(1))
