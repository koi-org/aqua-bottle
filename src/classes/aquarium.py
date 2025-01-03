from classes.fish import Fish


class Aquarium:
    """
    A class to represent an aquarium.

    ...
    Attributes
    ----------
    channel_id : int
        the channel id of where the aquarium is located
    cycled: bool
        checks if the aquarium is ammonia cycled
    volume : int
        the volume of the aquarium in litres
    substrate : str
        the substrate of the aquarium
    heater : bool
        checks whether the tank has a heater
    water_quality : dict
        the water quality of a tank, such as pollution, pH and temperature

    Methods
    --------
        choose_substrate(substrate):
            chooses the substrate for the aquarium
        add_heater():
            adds a heater to the aquarium
        add_fish(fish: Fish):
            adds fish to the aquarium
    """

    valid_fish = {"guppy", "neon_tetra", "molly", "platy"}
    valid_substrate = {"gravel", "sand", "soil"}

    def __init__(
        self,
        channel_id: int,
        volume: int,
    ):
        """
        Construcuts necessary attributes for the aquarium object.

        Parameters
        ---------
            channel_id : int
                the channel id of where the aquarium is located
            volume : int
                the volume of the aquarium in litres
        """

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

    def add_fish(self, fish: Fish):
        """
        Method to add fish to the aquarium

        Parameters
        ----------
        fish : Fish
            the fish that will be added

        Returns
        ------
        None
        """
        self.inhabitants["fish"].add(fish)

    def __eq__(self, other):
        if isinstance(other, Aquarium):
            return self.channel_id == other.channel_id
        return False

    def __hash__(self):
        return hash(self.channel_id)

    def __repr__(self):
        return f"Aquarium (channel_id={self.channel_id})"
