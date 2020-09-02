# -*- coding: utf-8 -*-

from flask import Flask

from src import configurations

config = configurations.get_config()

web_app = None


def get_web_app():
    global web_app
    if not web_app:
        web_app = Flask(__name__)
        web_app.config.from_object(config)
    return web_app
