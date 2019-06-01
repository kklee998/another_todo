from . import db, ma
from marshmallow import fields, validate


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
