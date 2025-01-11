from classes.aquarium import Aquarium


class Fish:
    VALID_FISH = {"Guppy", "Neon Tetra", "Molly", "Platy"}

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
        self.age = months
        self.hunger: int = 10
        self.hp: float = 100
        self.survivability = 100
        self.lifespan = 2 * Aquarium.YEAR
        self.alive: bool = True

    def __str__(self):
        return (
            f"specie: {self.species} gender: {self.gender} age (in months): {self.age} "
        )
