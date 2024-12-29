from user import User
from user_manager import UserManager


class Aquarium:
    def __init__(
        self,
        channel_id: int,
        volume: int,
    ):
        self.channel_id = channel_id
        self.cycled = False
        self.volume = volume
        self.substrate = None
        self.heater = False
        self.pollution = {"ammonia": 0, "nitrate": 0, "nitrite": 0}
        self.ph = None
        self.temperature = None
        self.plants = {}
        self.fish = {}

    def choose_substrate(self, substrate: str):
        self.substrate = substrate

    def add_heater(self):
        self.heater = True
