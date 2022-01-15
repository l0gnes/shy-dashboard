from quart import Quart
from quart_cors import cors
import asyncio

from prisma import Client, register

from blueprints import (
    api
)

app = Quart(__name__)
cors(
    app,
    allow_origin="*"
)

app.prisma = Client()
register(app.prisma)

app.register_blueprint(api.blueprint)

if __name__ == "__main__":

    # thank you robert
    asyncio.get_event_loop().run_until_complete(app.prisma.connect())

    app.run(
        host = "localhost",
        port = 6420
    )