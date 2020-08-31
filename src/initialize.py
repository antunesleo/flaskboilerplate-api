# -*- coding: utf-8 -*-

from flask import Flask
from flask_restx import Api

from src import configurations
from src import connections
from src.module_based_in_repository import endpoints as module1_endpoints
from src.module_based_in_repository.application_services import ItemsService
from src.module_based_in_repository.repositories import InMemoryItemRepository
from src.module_based_in_activerecord import endpoints as module2_endpoints

config = configurations.get_config()

web_app = Flask(__name__)
web_app.config.from_object(config)
api = Api(web_app)

connections.register(web_app)
elasticsearch_connection = connections.example2_elastic_search_connection

in_memory_item_repository = InMemoryItemRepository()
items_service = ItemsService(in_memory_item_repository)
module1_endpoints.register(api, items_service=items_service)

module2_endpoints.register(api)
