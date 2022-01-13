from flask import (
    Blueprint,
    jsonify
)
from helpers.quickResponses import QuickResponses

blueprint = Blueprint(
    "API", 
    __name__, 
    url_prefix="/api"
)

@blueprint.route("/ping")
def testEndpoint():
    return QuickResponses.pong()