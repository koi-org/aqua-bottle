from constants import Time
import random


class Fish:

    def __init__(self, species: str, gender: str, months: int):
        """
        Initialises fish instance with species gender and age in months

        Attributes:
            species: str
                the species of the fish
            gender: string
                gender of the fish
            age: int
                age of the person
            hp: int
                hp of a fish

        Methods
        ------
        TODO: add methods later
        """
        self.species = species
        self.gender = gender
        self.age = months * 30
        self.hunger: int = 10
        self.hp: float = 100
        self.survivability = 100
        self.lifespan = int(2 * (Time.YEAR / Time.UNIT))
        self.mature = False
        self.reproduce_chance = 0

        self.alive: bool = True
        self.starving = False

    def update(self, water_quality: float):
        # check water quality
        self.age += 1
        if self.mature:
            self.reproduce_chance += 5

        if self.hunger > 0:
            self.hunger -= 1

        if 50 <= water_quality < 70:
            self.hp -= 0.5
        elif water_quality < 50:
            self.hp -= 1

        # check hunger
        if 5 <= self.hunger <= 7:
            self.hp -= 0.5
        elif 0 < self.hunger < 5:
            self.hp -= 1
        elif self.hunger == 0 and not self.starving:
            # self is starving, add death penalty to the self
            self.survivability -= 33
            self.starving = True
        elif self.hunger != 0 and self.starving:
            self.survivability += 20
            self.starving = False

        curr_age_percent = (self.age / self.lifespan) * 100

        if 40 <= curr_age_percent < 50:
            self.mature = True
        if 50 <= curr_age_percent < 60:
            self.survivability -= 2
        elif 60 <= curr_age_percent < 70:
            self.survivability -= 3
        elif 70 <= curr_age_percent < 80:
            self.survivability -= 4
        elif 80 <= curr_age_percent < 90:
            self.survivability -= 5
        elif 90 <= curr_age_percent < 100:
            self.survivability -= 6
        elif curr_age_percent > 100:
            self.survivability -= 10

        if random.randint(1, 100) > self.survivability:
            self.alive = False

    def __str__(self):
        return (
            f"Fish Species: {self.species}\n"
            f"Gender: {self.gender}\n"
            f"Age: {self.age} days\n"
            f"Hunger: {self.hunger}\n"
            f"Health: {self.hp}%\n"
            f"Ready to breed: {self.mature}"
            f"Readiness to breed: {self.reproduce_chance}"
            f"Survivability: {self.survivability}%\n"
            f"Lifespan: {int(self.lifespan / 30)} months\n"
            f"Alive: {'Yes' if self.alive else 'No'}"
        )
