from classes.aquarium import Aquarium
from typing import Set


class User:
    """
    Represents a user in the system who owns aquariums.

    Attributes:
        name (str): The name of the user.
        id (int): A unique identifier for the user.
        aquariums (Set[Aquarium]): A set of aquariums owned by the user.
        balance (float): The user's account balance.
    """

    def __init__(self, name: str, id: int, balance: float):
        """
        Initializes a User object.

        Parameters:
            name (str): The name of the user.
            id (int): A unique identifier for the user.
            balance (float): The user's starting account balance.
        """
        self.name = name
        self.id = id
        self.aquariums: Set[Aquarium] = set()
        self.balance = balance

    def __str__(self):
        """
        Returns a string representation of the user.

        Returns:
            str: The user's name and balance in the format 'name (balance)'.
        """
        return f"{self.name} ({self.balance})"

    def add_aquarium(self, aquarium: Aquarium):
        """
        Adds an aquarium to the user's collection.

        Parameters:
            aquarium (Aquarium): The aquarium to add.

        Returns:
            bool: True if the aquarium was added, False if it was already in the collection.
        """
        if aquarium in self.aquariums:
            return False
        self.aquariums.add(aquarium)
        return True

    def remove_aquarium(self, aquarium: Aquarium):
        """
        Removes an aquarium from the user's collection.

        Parameters:
            aquarium (Aquarium): The aquarium to remove.

        If the aquarium does not exist in the user's collection, prints an error message.
        """
        if aquarium not in self.aquariums:
            print("Aquarium doesn't exist")
        self.aquariums.discard(aquarium)

    def get_aquarium(self, channel_id: int):
        """
        Retrieves an aquarium by its channel ID.

        Parameters:
            channel_id (int): The channel ID of the aquarium to retrieve.

        Returns:
            Aquarium: The aquarium with the matching channel ID, or None if not found.
        """
        for aquarium in self.aquariums:
            if aquarium.channel_id == channel_id:
                return aquarium
