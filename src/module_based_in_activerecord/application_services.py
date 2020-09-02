from typing import List
from src.base.application_services import ApplicationService
from src.module_based_in_activerecord.models import Example


class ExampleService(ApplicationService):
    example_active_record = Example

    def create_example(self, example_dict: dict) -> None:
        self.example_active_record.add(example_dict)

    def list_example(self) -> List[dict]:
        examples_dict = []
        for example in self.example_active_record.list():
            examples_dict.append({
                'id': example.id,
                'name': example.name
            })
        return examples_dict
