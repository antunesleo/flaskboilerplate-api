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

    @api.marshal_with(serializers.items_serializer, as_list=True)
    @api.doc(responses={500: 'Sorry dude, its my fault', 400: 'Dude, what are you saying?'})
    def get(self):
        try:
            items = self.__items_service.list_items()
            return items
        except Exception:
            api.abort(400, 'My custom message', custom='value')


    def post(self):
        try:
            self.__items_service.create_item({'id': 3, 'name': 'alkk ei'})
            return self._return_success_created()
        except Exception:
            return self._return_unexpected_error()

    @not_allowed
    def put(self):
        pass

    @not_allowed
    def delete(self):
        pass


def register(items_service):
    api.add_resource(ItemsResource, '/api/items', resource_class_kwargs={'items_service': items_service})
