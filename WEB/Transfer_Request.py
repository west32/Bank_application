from marshmallow import Schema, fields


class TransferRequest(Schema):
    a_account = fields.String(required=True)
    b_account = fields.String(required=True)
    money_amount = fields.Float(required=True)