from flask import (
    Blueprint,
    jsonify
)

blueprint = Blueprint(
    "API", 
    __name__, 
    url_prefix="/api"
)

@blueprint.route("/test")
def testEndpoint():
    return jsonify(
        {
            "status" : 200
        }
    )