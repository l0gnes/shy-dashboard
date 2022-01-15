from quart import (
    jsonify,
    Response
)
from enum import Enum

class QuickResponses(object):
    """
        A simpler method of returning basic json responses where they are needed.
        More than likely will be used mainly for error responses within the API.
    """
    
    @staticmethod
    def pong() -> Response:
        return jsonify(
            {
                "status" : 200,
                "message" : "Pong!"
            }
        )

    @staticmethod
    def userAlreadyExists() -> Response:
        return jsonify(
            {
                "status" : 400,
                "message" : "User already exists"
            }
        )