from user import User
from user_manager import UserManager


class Aquarium:
    aquarium_data = []
    def __init__(self, user_id: int, channel_id: int):
        self.user_id = user_id
        self.channel_id = channel_id
        self.cycled = False

        if self.aquarium_exists():
            raise ValueError("Aquarium already exists")
        else:
            Aquarium.aquarium_data.append(self)    

    def aquarium_exists(self):
        for aquarium in Aquarium.aquarium_data:
            if aquarium.channel_id == self.channel_id:
                return True
        return False
    

# user1 = User(name="Son Doumeg", user_id = 59, aquarium=None, balance=999)
# print(user1)

# doumeg_id = user1.user_id
# channel_id = 69

# aquarium1 = Aquarium(69, channel_id)
# aquarium1 = Aquarium(69, channel_id)