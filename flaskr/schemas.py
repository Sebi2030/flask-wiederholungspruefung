from marshmallow import Schema, fields, validates_schema, ValidationError

class PostSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    body = fields.Str(required=True)
    created = fields.DateTime(dump_only=True)
    author_id = fields.Int(required=True)

class PostUpdateSchema(Schema):
    title = fields.Str()
    body = fields.Str()
    author_id = fields.Int()
    