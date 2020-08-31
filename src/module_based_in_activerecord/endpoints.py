from src.base.endpoints import ResourceBase, not_allowed


class Module2ItemsResource(ResourceBase):

    def get(self):
        response = self._converter.snake_to_camel({'how_are_you': 'i am module_based_in_activerecord and im good'})
        return response, 200

    @not_allowed
    def post(self):
        pass

    @not_allowed
    def put(self):
        pass

    @not_allowed
    def delete(self):
        pass


def register(api):
    api.add_resource(Module2ItemsResource, '/api/module_based_in_activerecord-items')
