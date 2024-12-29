valid_fish = {
    "guppy",
    "neon_tetra",
    "molly",
    "platy"
}


"""
    This class contains the information and stats of a fish
"""
class Fish:
    def __init__(self, species, gender, age_months):

        if species not in valid_fish:
            print("Invalid species")
        else:
            self.species = species
            self.gender = gender
            self.age = age_months

    def __str__(self):
        return f"specie: {self.species} gender: {self.gender} age (in months): {self.age} "