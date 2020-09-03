# -*- coding: utf-8 -*-

from src import configurations, web_app as web_app_module
from src import connections
from src.module_based_in_repository import endpoints as module1_endpoints
from src.module_based_in_repository.application_services import ItemsService
from src.module_based_in_repository.repositories import InMemoryItemRepository
from src.module_based_in_activerecord import endpoints as module2_endpoints

config = configurations.get_config()
web_app = web_app_module.get_web_app()
api = web_app_module.get_api()

connections.register(web_app)
elasticsearch_connection = connections.example2_elastic_search_connection

in_memory_item_repository = InMemoryItemRepository()
items_service = ItemsService(in_memory_item_repository)
module1_endpoints.register(items_service=items_service)

module2_endpoints.register()
