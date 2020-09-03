from abc import ABC, abstractmethod
from typing import List

from src.base.domain import AggregateRoot


class Item(AggregateRoot):

    def __init__(self, id: int, name: str, full_info: str):
        self.__id = id
        self.__name = name
        self.__full_info = full_info

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def full_info(self):
        return self.__full_info


class ItemRepository(ABC):

    @abstractmethod
    def list(self, for_read=True) -> List[Item]:
        raise NotImplementedError

    @abstractmethod
    def add(self, question: Item) -> None:
        raise NotImplementedError
