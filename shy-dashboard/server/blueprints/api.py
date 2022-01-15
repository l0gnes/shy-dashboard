from quart import (
    Blueprint,
    jsonify,
    request,
    current_app
)
from helpers.quickResponses import QuickResponses

from helpers.converters import UserFormatter

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

        userid = request.json['userid']

        
        existenceCheck = await User.prisma().find_first(
            where = {
                "user" : userid
            }
        )

        if not existenceCheck:

            
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


