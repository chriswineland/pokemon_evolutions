from flask import Flask, Request, Response, jsonify, make_response
from enum import Enum


class ResponseInfo(Enum):
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message


class ErrorInfo(ResponseInfo):
    pass


class SuccessInfo(ResponseInfo):
    pass


class BaseRestService:
    def __init__(self, app: Flask):
        pass

    def service(self, request: Request):
        pass

    def http_route() -> str:
        pass

    def http_methods() -> list[str]:
        pass

    @staticmethod
    def error_response(error: ErrorInfo) -> Response:
        response = make_response(jsonify({}))
        response.status_code = error.code
        response.headers['message'] = error.message
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response

    @staticmethod
    def successful_response(body: dict, info: SuccessInfo | None = None) -> Response:
        response = make_response(jsonify(body))
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        response.headers['mimetype'] = 'application/json'
        response.headers['Access-Control-Allow-Origin'] = '*'
        if info is not None:
            response.status_code = info.code
            response.headers['message'] = info.message
        else:
            response.status_code = 200
        return response