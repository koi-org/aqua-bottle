from user import User
from user_manager import UserManager


class Aquarium:
    def __init__(self, user: User, channel_id: int):
        self.user_id = user.id
        self.channel_id = channel_id
        self.cycled = False

        if not UserManager.user_exists(self.user_id):
            raise ValueError("User does not exist")
        elif self.aquarium_exists(user, channel_id):
            raise ValueError("Aquarium exists")
        else:
            self.append_aquarium(self.user_id)


    def aquarium_exists(self, user: User, channel_id):
        for aquarium in user.aquariums:
            if aquarium.channel_id == channel_id:
                return True
            return False


    def append_aquarium(self, user_id):
        for user in UserManager.users:
            if user.id == user_id:
                user.aquariums.append(self)