from Server.rest.base_rest_service import BaseRestService, SuccessInfo
from flask import Flask, Request, request


class Example(BaseRestService):
    def __init__(self, app: Flask):
        super().__init__(app)
        @app.route(self.http_route(), methods=self.http_methods())
        def example():
            return self.service(request)

    def service(self, request: Request):
        return self.successful_response({"exmaple": True})

    def http_route(self) -> str:
        return "/"

    def http_methods(self) -> list[str]:
        return ["get"]