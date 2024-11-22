from flask import Flask
from Server.rest.example import Example
from Server.rest.base_rest_service import BaseRestService


def add_rest_services(app: Flask):
    rest_services: list[BaseRestService] = [
        Example(app)
    ]
    