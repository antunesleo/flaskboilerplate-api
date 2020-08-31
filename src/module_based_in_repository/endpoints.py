from src.base.endpoints import ResourceBase, not_allowed
from src.module_based_in_repository.application_services import ItemsService


class ItemsResource(ResourceBase):

    def __init__(self, items_service: ItemsService):
        super(ItemsResource, self).__init__()
        self.__items_service = items_service

    def get(self):
        items_dict = self.__items_service.list_items()
        response = self._converter.snake_to_camel(items_dict)
        return response, 200

    def post(self):
        self.__items_service.create_item({'id': 3, 'name': 'alkk ei'})
        return self._converter.snake_to_camel({'result': 'Created'}), 201

    @not_allowed
    def put(self):
        pass

    @not_allowed
    def delete(self):
        pass


def register(api, items_service):
    api.add_resource(ItemsResource, '/api/items', resource_class_kwargs={'items_service': items_service})
