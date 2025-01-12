from classes.fish import Fish
from classes.plant import Plant
from classes.decoration import Decoration
from constants import Time
from typing import Set
import datetime
import threading
import time
import random


class Aquarium:

    def __init__(self, channel_id: int, volume: int, substrate: str):
        self.channel_id = channel_id
        self.volume = volume
        self.substrate = substrate
        self.start_cycle = None
        self.cycled = False
        self.water_quality = 100
        self.fish: Set[Fish] = set()
        self.plants: Set[Plant] = set()
        self.decoration: Set[Decoration] = set()

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
        self.fish.add(fish)

    def add_plant(self, plant: Plant):
        """
        Method to add plant

        Parameters
        ---------
        plant: Plant
        """
        self.plants.add(plant)

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
        if len(self.fish) == 0:
            self.start_cycle = datetime.datetime.now()
        else:
            for fish in self.fish:
                fish.hunger += 6
                if fish.hunger > 10:
                    fish.hunger = 10

    def monitor_water(self, current_time: datetime):
        if not self.start_cycle:
            return

        if current_time - self.start_cycle > datetime.timedelta(seconds=15):
            self.cycled = True

        water_quality_decrement_multiplier = 1

        if len(self.plants) > 0:
            water_quality_decrement_multiplier = 0.5

        if not self.cycled:
            self.water_quality -= 3 * water_quality_decrement_multiplier
        else:
            self.water_quality -= 1 * water_quality_decrement_multiplier

        if self.water_quality < 0:
            self.water_quality = 0

    def monitor_fish(self):
        for fish in list(self.fish):
            fish.update(self.water_quality)

    def purge_fish(self):
        for fish in list(self.fish):
            if not fish.alive:
                print("Fish has been removed!")
                self.fish.discard(fish)
                # discard fish

    def add_decoration(self, decoration: Decoration):
        self.decoration.add(decoration)

    def update_timer(self):
        while self.running:
            current_time = datetime.datetime.now()

            delta = current_time - self.birth_date
            self.age = int(delta.total_seconds() // Time.UNIT)
            self.debug_timer()

            self.monitor_water(current_time)
            self.monitor_fish()
            self.purge_fish()

            time.sleep(Time.UNIT)

    def debug_timer(self):
        print(
            f"The aquarium in channel: {self.channel_id} is {self.age} time units old.\n"
            f"Cycled? {self.cycled}\n"
            f"Water quality: {self.water_quality}\n"
            f"---"
        )

        for fish in self.fish:
            print(f"{fish}\n" f"---\n")

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
