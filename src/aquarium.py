from user import User
from user_manager import UserManager


class Aquarium:
    def __init__(self, user, channel_id: int):
        self.channel_id = channel_id
        self.cycled = False

        if not UserManager.user_exists(user.id):
            raise ValueError("User does not exist")
        if self.aquarium_exists(user, channel_id):
            raise ValueError("Aquarium exists")

    def aquarium_exists(self, user: User, channel_id: int):
        for aquarium in user.aquariums:
            if aquarium.channel_id == channel_id:
                return True
            return False
