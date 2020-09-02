from abc import ABC, abstractmethod
from typing import List

from src.base.domain import AggregateRoot


class Item(AggregateRoot):

    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name


class ItemRepository(ABC):

    @abstractmethod
    def list(self, for_read=True) -> List[Item]:
        raise NotImplementedError

    @abstractmethod
    def add(self, question: Item) -> None:
        raise NotImplementedError
