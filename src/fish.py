"""
    This class contains the information and stats of a fish
"""


class Fish:
    def __init__(self, species, gender, age_months):
        self.species = species
        self.gender = gender
        self.age = age_months

    def __str__(self):
        return (
            f"specie: {self.species} gender: {self.gender} age (in months): {self.age} "
        )
