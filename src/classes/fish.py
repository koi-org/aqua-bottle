class Fish:
    """
    A class to represent fish
    """

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

        Methods
        ------
        TODO: add methods later
        """
        self.species = species
        self.gender = gender
        self.age = age_months

    def __str__(self):
        return (
            f"specie: {self.species} gender: {self.gender} age (in months): {self.age} "
        )
