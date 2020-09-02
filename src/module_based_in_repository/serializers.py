import json
import yaml

from src.base.serializers import JSONSerializer, YAMLSerializer
from src.base.serializers import  CaseStyleConverter
from src.module_based_in_repository.domain import Item


class ItemSerializer(JSONSerializer, YAMLSerializer):
    converter = CaseStyleConverter()

    def serialize_json(self, item, many=False) -> dict:
        if many:
            converted_dict = [self.converter.snake_to_camel(self.__item_to_dict(x)) for x in item]
        else:
            converted_dict = self.converter.snake_to_camel(self.__item_to_dict(item))

        return converted_dict

    def deserialize_json(self, string_json: str) -> dict:
        return self.converter.camel_to_snake(json.loads(string_json))

    def serialize_yaml(self, item: Item, many=False) -> str:
        if many:
            converted_item = [self.__item_to_dict(x) for x in item]
        else:
            converted_item = self.__item_to_dict(item)
        return yaml.dump(converted_item)

    def deserialize_yaml(self, string_yaml: str) -> dict:
        return yaml.load(string_yaml)

    def __item_to_dict(self, item: Item):
        return {'id': item.id, 'name': item.name}
