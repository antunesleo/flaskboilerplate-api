from typing import List

from src.module_based_in_repository.domain import ItemRepository, Item


class InMemoryItemRepository(ItemRepository):

    def __init__(self):
        self.__items = [
            Item('kdao wrgf', 'kfposakopfskpod', 1),
            Item('hdasu kqp', 'fdfsakfkpaosfko', 1)
        ]

    def add(self, item: Item) -> None:
        self.__items.append(item)

    def list(self, for_read=True) -> List[Item]:
        return self.__items
