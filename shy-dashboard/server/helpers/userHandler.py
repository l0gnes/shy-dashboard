from prisma.models import User

class UserFormatter(object):

    @staticmethod
    def convert(user : User) -> dict:
        return {
            "userid" : user.user,
            "gold" : user.gold,
            "health" : user.health,
            "pronoums" : user.pronouns,
            "experience" : user.experience
        }