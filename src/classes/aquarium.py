from classes.fish import Fish
from classes.plant import Plant
from classes.decoration import Decoration
import datetime
import threading
import time


class Aquarium:
    VALID_SUBSTRATE = {"Gravel", "Sand", "Soil"}
    VALID_DECORATION = {"driftwood", "rock"}
    TIME_UNIT = 5

    def __init__(self, channel_id: int, volume: int, substrate: str):
        self.channel_id = channel_id
        self.volume = volume
        self.substrate = substrate
        self.start_cycle = None
        self.cycled = False
        self.water_quality = 100
        self.inhabitants = {"fish": set(), "plants": set()}
        self.decoration = set()

        # timer
        self.birth_date = datetime.datetime.now()
        self.age = 0
        self.running = True
        self.timer_thread = threading.Thread(target=self.update_timer)
        self.timer_thread.start()

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
        self.inhabitants["plants"].add(plant)

    def water_change(self, litres):
        if litres > self.volume:
            return False

        self.water_quality = self.new_water_quality(litres)
        return True

    def new_water_quality(self, litres):
        quality_old = self.water_quality
        quality_new = 100
        volume_old = self.volume - litres
        volume_new = litres

        new_quality_numerator = (quality_old * volume_old) + (quality_new * volume_new)
        new_quality_denominator = volume_new + volume_old

        return new_quality_numerator / new_quality_denominator

    def feed(self):
        if len(self.inhabitants["fish"]) == 0:
            self.start_cycle = datetime.datetime.now()
        else:
            for fish in self.inhabitants["fish"]:
                fish.fed = True

    def monitor_water(self):
        water_quality_decrement_multiplier = 1

        if len(self.inhabitants["plants"]) > 0:
            water_quality_decrement_multiplier = 0.5

        if not self.cycled:
            self.water_quality -= 3 * water_quality_decrement_multiplier
        else:
            self.water_quality -= 1 * water_quality_decrement_multiplier

        if self.water_quality < 0:
            self.water_quality = 0

    def add_decoration(self, decoration: Decoration):
        self.decoration.add(decoration)

    def update_timer(self):
        while self.running:
            current_time = datetime.datetime.now()

            delta = current_time - self.birth_date
            self.age = int(delta.total_seconds() // Aquarium.TIME_UNIT)
            self.debug_timer()

            # monitor water
            if self.start_cycle:
                if current_time - self.start_cycle > datetime.timedelta(seconds=15):
                    self.cycled = True
                self.monitor_water()

            time.sleep(1)

    def debug_timer(self):
        print(
            f"The aquarium in channel: {self.channel_id} is {self.age} time units old.\n"
            f"Cycled? {self.cycled}\n"
            f"Water quality: {self.water_quality}\n"
            f"---"
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
