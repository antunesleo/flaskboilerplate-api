
class Example:
    id = None
    name = None

    @classmethod
    def add(cls, example_dict: dict):
        pass

    @classmethod
    def list(cls):
        for id in range(0, 3):
            example = cls()
            example.id = id
            example.name = 'fdjsaoi ejikpo'

            yield cls(id, 'fdjsaoi ejikpo')

    def change_name(self, name):
        pass
