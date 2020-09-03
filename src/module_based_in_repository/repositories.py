from typing import List

from src.module_based_in_repository.domain import ItemRepository, Item


class InMemoryItemRepository(ItemRepository):

    def __init__(self):
        self.__items = [
            Item(1, 'kdao wrgf', 'kfposakopfskpod'),
            Item(2, 'hdasu kqp', 'fdfsakfkpaosfko')
        ]

    def add(self, item: Item) -> None:
        self.__items.append(item)

    def list(self, for_read=True) -> List[Item]:
        return self.__items
