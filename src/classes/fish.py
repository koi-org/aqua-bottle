from classes.aquarium import Aquarium


class Fish:
    time_unit = Aquarium.TIME_UNIT
    aq_year = 365 * time_unit
    aq_month = 30 * time_unit
    VALID_FISH = {"Guppy", "Neon Tetra", "Molly", "Platy"}

    def __init__(self, species: str, gender: str, age_months: int):
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
        self.age = Fish.aq_month * age_months
        self.hunger: int = 10
        self.hp: float = 100
        self.survivability = 100
        self.lifespan = 2 * Fish.aq_year
        self.alive: bool = True

    def __str__(self):
        return (
            f"specie: {self.species} gender: {self.gender} age (in months): {self.age} "
        )
