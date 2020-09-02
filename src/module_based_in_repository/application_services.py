from typing import List
from src.base.application_services import ApplicationService
from src.module_based_in_repository.domain import Item, ItemRepository


class ItemsService(ApplicationService):

    def __init__(self, repository: ItemRepository):
        self.__repository = repository

    def create_item(self, item_dict: dict) -> None:
        item = Item(**item_dict)
        self.__repository.add(item)

    def list_items(self) -> List[Item]:
        return self.__repository.list()

