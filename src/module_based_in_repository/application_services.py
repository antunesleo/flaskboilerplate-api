from typing import List
from src.base.application_services import ApplicationService
from src.module_based_in_repository.domain import Item


class ItemsService(ApplicationService):

    def __init__(self, repository):
        self.__repository = repository

    def create_item(self, item_dict: dict) -> None:
        item = Item(**item_dict)
        self.__repository.add(item)

    def list_items(self) -> List[dict]:
        items_dict = []
        for item in self.__repository.list():
            items_dict.append({
                'id': item.id,
                'name': item.name
            })
        return items_dict
