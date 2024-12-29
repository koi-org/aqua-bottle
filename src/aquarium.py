"""
This module defines the Aquarium class, which simulates an aquarium's features 
and provides methods to manage its environment.
"""
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
            "temperature": None
            }
        self.inhabitants = {
            'fish': {},
            'plants': {}
        }

    def choose_substrate(self, substrate: str):
        """Method to choose the aquarium's substrate"""
        self.substrate = substrate

    def add_heater(self):
        """Method to add a heater to the fish tank"""
        self.heater = True
