import re
from functools import wraps

from flask_restx import Resource
from flask import Response, request


class ResourceBase(Resource):

    def __init__(self,  *args, **kwargs):
        super(ResourceBase, self).__init__( *args, **kwargs)

    def _get_payload(self):
        payload = {}
        if request.json:
            payload.update(self._converter.camel_to_snake(request.json))
        if request.form:
            payload.update(self._converter.camel_to_snake(request.form))
        return payload

    def _get_query_string(self):
        query_string = {}
        if request.args:
            query_string.update(self._converter.camel_to_snake(request.args))
        return query_string

    @staticmethod
    def _get_files():
        return request.files

    @staticmethod
    def _return_unexpected_error():
        return {'result': 'error', 'error': 'Internal Server Error', 'exception': 'An unexpected error occurred'}, 500

    @staticmethod
    def _return_success_created():
        return {'result': 'Created'}, 201


def not_allowed(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        return Response('{"result": "Method not allowed"}', 405, content_type='application/json')
    return decorated_function
