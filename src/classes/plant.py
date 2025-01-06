class Plant:

    VALID_PLANTS = [
        "java_fern" "java_moss",
        "anubias",
    ]
    """
    Represents a plant species.

    This class validates whether the given species is part of the predefined
    list of valid plants and initializes the plant if valid.
    """

    def __init__(self, species):
        """
        Initializes a Plant object.

        Parameters:
        species (str): The species of the plant to be validated.

        Prints an error message if the species is not in the valid plants list.
        """
        self.species = species
