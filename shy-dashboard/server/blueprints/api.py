from flask import (
    Blueprint,
    jsonify,
    request,
    current_app
)
from itsdangerous import json
from helpers.quickResponses import QuickResponses

from helpers.userHandler import UserFormatter

from prisma.models import (
    User
)

blueprint = Blueprint(
    "API", 
    __name__, 
    url_prefix="/api"
)

@blueprint.route("/ping")
async def testEndpoint():
    return QuickResponses.pong()

@blueprint.route("/user/<int:userid>", methods=["GET"])
@blueprint.route("/user", methods=["POST"])
async def userEndpoint(userid : int = None):

    if request.method == "GET":

        async with current_app.prisma:
            userData = await User.prisma().find_first(
                where = {
                    'user' : userid
                }
            )

        return jsonify(
            UserFormatter.convert(
                userData
            )
        )

    elif request.method == "POST":

        userid = request.args['userid']

        async with current_app.prisma:
            existenceCheck = await User.prisma().find_first(
                where = {
                    "user" : userid
                }
            )

        if not existenceCheck:

            async with current_app.prisma:
                newUser = await User.prisma().create(
                    data = {
                        "user" : userid 
                    }
                )

            return jsonify(
                UserFormatter.convert(
                    newUser
                )
            )

        else:

            return QuickResponses.userAlreadyExists()


