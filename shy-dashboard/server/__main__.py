from pydoc import resolve
from flask import Flask
from flask_cors import CORS

from blueprints import (
    api
)

app = Flask(__name__)
CORS(
    app,
    resources = {r'/*' : {'origins' : '*'}}
)

app.register_blueprint(api.blueprint)

if __name__ == "__main__":
    app.run(
        host = "localhost",
        port = 6420
    )