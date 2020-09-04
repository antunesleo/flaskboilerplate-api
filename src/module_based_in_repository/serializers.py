from flask_restx import fields, reqparse

from src.web_app import get_api


api = get_api()


item_model = api.model('Item', {
    'id': fields.Integer,
    'name': fields.String,
    'fullInfo': fields.String(attribute='full_info')
})

item_creation_parser = reqparse.RequestParser()
item_creation_parser.add_argument('name', type=str, required=True, location='json')
item_creation_parser.add_argument('fullInfo', type=str, dest='full_info', required=True, location='json')
item_creation_parser.add_argument('shouldDoSomething', dest='should_do_something', type=bool, required=True)
