from fish import Fish

"""
This module defines the Aquarium class, which simulates an aquarium's features 
and provides methods to manage its environment.
"""

valid_substrate = {"gravel", "sand", "soil"}


valid_fish = {"guppy", "neon_tetra", "molly", "platy"}


class Aquarium:
    """The aquarium class"""

    def __init__(
        self,
        channel_id: int,
        volume: int,
    ):
        """Init method to create an aquarium"""
        self.channel_id = channel_id
        self.cycled = False
        self.volume = volume
        self.substrate = None
        self.heater = False
        self.water_quality = {
            "ammonia": 0,
            "nitrate": 0,
            "nitrite": 0,
            "ph": None,
            "temperature": None,
        }
        self.inhabitants = {"fish": set(), "plants": set()}

    def choose_substrate(self, substrate: str):
        """Method to choose the aquarium's substrate"""
        self.substrate = substrate

    def add_heater(self):
        """Method to add a heater to the fish tank"""
        self.heater = True

    def is_valid_fish(self, fish: Fish):
        if fish.species not in valid_fish:
            return False
        return True

    def add_fish(self, fish: Fish):
        self.inhabitants["fish"].add(fish)
