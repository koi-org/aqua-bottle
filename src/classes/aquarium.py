from classes.fish import Fish
from classes.plant import Plant
import datetime
import threading
import time

valid_substrate = {"Gravel", "Sand", "Soil"}
valid_decoration = {"driftwood", "rock"}


class Aquarium:
    time_unit = 5

    def __init__(self, channel_id: int, volume: int, substrate: str):
        self.channel_id = channel_id
        self.cycled = False
        self.volume = volume
        self.substrate = substrate
        self.heater = False
        self.water_quality = 100
        self.inhabitants = {"fish": set(), "plants": set()}
        self.decoration = set()

        # timer
        self.birth_date = datetime.datetime.now()
        self.age = 0
        self.running = True
        self.timer_thread = threading.Thread(target=self.update_age)
        self.timer_thread.start()

    # def add_heater(self):
    #     """Method to add a heater to the fish tank"""
    #     self.heater = True

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

    def add_plant(self, plant: Plant):
        """
        Method to add plant

        Parameters
        ---------
        plant: Plant
        """
        self.inhabitants["plant"].add(plant)

    def feed(self):
        if self.inhabitants["fish"] == set():
            self.water_quality -= 10
        else:
            for fish in self.inhabitants["fish"]:
                fish.fed = True

    def add_decoration(self, decoration):
        self.decoration.add(decoration)

    def update_age(self):
        while self.running:
            current_time = datetime.datetime.now()
            delta = current_time - self.birth_date
            self.age = int(delta.total_seconds() // Aquarium.time_unit)

            self.print_age()

            time.sleep(Aquarium.time_unit)

    def print_age(self):
        print(
            f"The aquarium in channel: {self.channel_id} is {self.age} time units old."
        )

    def stop(self):
        self.running = False
        self.timer_thread.join()

    def __eq__(self, other):
        if isinstance(other, Aquarium):
            return self.channel_id == other.channel_id
        return False

    def __hash__(self):
        return hash(self.channel_id)

    def __repr__(self):
        return f"Aquarium (channel_id={self.channel_id})\nBirth date:{self.birth_date}"
