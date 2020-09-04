from flask_restx import fields, marshal

from src.web_app import get_api

from src.base.endpoints import ResourceBase, not_allowed
from src.module_based_in_repository import serializers


api = get_api()


@api.doc()
class ItemsResource(ResourceBase):

    def __init__(self, *args, **kwargs):
        super(ItemsResource, self).__init__(*args, **kwargs)
        self.__items_service = kwargs['items_service']

    @api.marshal_list_with(serializers.item_model)
    @api.doc(responses={500: 'Sorry dude, its my fault', 400: 'Dude, what are you saying?'})
    def get(self):
        try:
            items = self.__items_service.list_items()
            return items
        except Exception:
            api.abort(400, 'My custom message', custom='value')

    @api.expect(serializers.item_creation_parser)
    def post(self):
        self.__items_service.create_item(serializers.item_creation_parser.parse_args())
        return self._return_success_created()

    @not_allowed
    def put(self):
        pass

    @not_allowed
    def delete(self):
        pass


def register(items_service):
    api.add_resource(ItemsResource, '/api/items', resource_class_kwargs={'items_service': items_service})
