from flask import Response

from src.base.endpoints import ResourceBase, not_allowed
from src.module_based_in_repository.serializers import ItemSerializer


class ItemsResource(ResourceBase):

    def __init__(self, *args, **kwargs):
        super(ItemsResource, self).__init__()
        self.__items_service = kwargs['items_service']
        self.__serializer = ItemSerializer()

    def get(self):
        try:
            items = self.__items_service.list_items()
            serialized_items = self.__serializer.serialize_yaml(items, many=True)
            return Response(serialized_items, mimetype='text/yaml')
        except Exception:
            return self._return_unexpected_error()

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


def register(api, items_service):
    api.add_resource(ItemsResource, '/api/items', resource_class_kwargs={'items_service': items_service})
