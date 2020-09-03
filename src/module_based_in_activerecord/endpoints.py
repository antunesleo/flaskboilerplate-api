from src.web_app import get_api
from src.base.endpoints import ResourceBase, not_allowed


api = get_api()


class Module2ItemsResource(ResourceBase):

    @not_allowed
    def get(self):
        pass

    @not_allowed
    def post(self):
        pass

    @not_allowed
    def put(self):
        pass

    @not_allowed
    def delete(self):
        pass


def register():
    api.add_resource(Module2ItemsResource, '/api/module_based_in_activerecord-items')
