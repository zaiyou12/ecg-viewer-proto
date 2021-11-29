from marshmallow import Schema, fields

class UserSchema(Schema):
    email = fields.Email()
    created_time = fields.DateTime()


class EcgTestSchema(Schema):
    region = fields.String()
    start_time = fields.DateTime()
    end_time = fields.DateTime()
    duration = fields.Integer()
    updated_time = fields.DateTime()
