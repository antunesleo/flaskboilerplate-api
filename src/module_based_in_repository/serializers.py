from flask_restx import fields

from src.web_app import get_api


api = get_api()


items_serializer = api.model('Item', {
    'id': fields.Integer,
    'name': fields.String,
    'fullInfo': fields.String(attribute='full_info')
})
