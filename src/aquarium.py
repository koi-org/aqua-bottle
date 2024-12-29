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
        self.pollution = {"ammonia": 0, "nitrate": 0, "nitrite": 0}
        self.ph = None
        self.temperature = None
        self.plants = {}
        self.fish = {}

    def choose_substrate(self, substrate: str):
        """Method to choose the aquarium's substrate"""
        self.substrate = substrate

    def add_heater(self):
        """Method to add a heater to the fish tank"""
        self.heater = True
