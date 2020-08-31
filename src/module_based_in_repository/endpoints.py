from src.base.endpoints import ResourceBase, not_allowed
from src.module_based_in_repository.application_services import ItemsService


class ItemsResource(ResourceBase):

    def __init__(self, items_service: ItemsService):
        super(ItemsResource, self).__init__()
        self.__items_service = items_service

    def get(self):
        try:
            items_dict = self.__items_service.list_items()
            return self._converter.snake_to_camel(items_dict), 200
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
