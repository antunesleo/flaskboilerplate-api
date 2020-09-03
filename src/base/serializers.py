"""Generic serializers and converters that can be used for any component"""
import json
import re
from abc import ABC, abstractmethod
from typing import Callable

import yaml
from rest_framework.serializers import Serializer


class CaseStyleConverter(object):

    def __camel_to_snake(self, name: str) -> str:
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

    def __snake_to_camel(self, name: str) -> str:
        result = []
        for index, part in enumerate(name.split('_')):
            if index == 0:
                result.append(part.lower())
            else:
                result.append(part.capitalize())
        return ''.join(result)

    def __transform_key(self, data: dict, method: Callable) -> dict:
        if isinstance(data, dict):
            return {method(key): self.__transform_key(value, method) for key, value in data.items()}
        if isinstance(data, list):
            for index, item in enumerate(data):
                if isinstance(item, dict):
                    data[index] = {method(key): self.__transform_key(value, method) for key, value in item.items()}
        return data

    def camel_to_snake(self, data_dict: dict) -> dict:
        return self.__transform_key(data_dict, self.__camel_to_snake)

    def snake_to_camel(self, data_dict: dict) -> dict:
        return self.__transform_key(data_dict, self.__snake_to_camel)


class JSONSerializer(ABC):

    @abstractmethod
    def serialize_json(self, object: object, many=False) -> str:
        raise NotImplementedError

    @abstractmethod
    def deserialize_json(self, string_json: str) -> dict:
        raise NotImplementedError


class YAMLSerializer(ABC):

    @abstractmethod
    def serialize_yaml(self, object: object, many=False) -> str:
        raise NotImplementedError

    @abstractmethod
    def deserialize_yaml(self, string_yaml: str) -> dict:
        raise NotImplementedError


class GenericSerializer(JSONSerializer, YAMLSerializer):
    converter = CaseStyleConverter()

    def __init__(self, middleware_serializer_class: Serializer):
        self.__middleware_serializer_class = middleware_serializer_class

    def serialize_json(self, object: object, many=False) -> str:
        serializer = self.__middleware_serializer_class(object, many=many)
        return json.dumps(serializer.data)

    def deserialize_json(self, string_json: str) -> dict:
        pass

    def serialize_yaml(self, object: object, many=False) -> str:
        serializer = self.__middleware_serializer_class(object, many=many)
        if many:
            return yaml.dump([dict(item) for item in serializer.data])
        return yaml.dump(serializer.data)

    def deserialize_yaml(self, string_yaml: str) -> dict:
        pass
