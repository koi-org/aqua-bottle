from classes.fish import Fish
import datetime
import threading
import time


valid_fish = {"Guppy", "Neon Tetra", "Molly", "Platy"}
valid_substrate = {"Gravel", "Sand", "Soil"}


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

    time_unit = 5

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

        # timer
        self.birth_date = datetime.datetime.now()
        self.age = 0
        self.running = True
        self.timer_thread = threading.Thread(target=self.update_age)
        self.timer_thread.start()

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

    def update_age(self):
        while self.running:
            current_time = datetime.datetime.now()
            delta = current_time - self.birth_date
            self.age = int(delta.total_seconds() // Aquarium.time_unit)

            self.print_age()

            time.sleep(Aquarium.time_unit)

    def __eq__(self, other):
        if isinstance(other, Aquarium):
            return self.channel_id == other.channel_id
        return False

    def __hash__(self):
        return hash(self.channel_id)

    def __repr__(self):
        return f"Aquarium (channel_id={self.channel_id})\nBirth date:{self.birth_date}"
