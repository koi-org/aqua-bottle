from classes.user import User
from typing import Dict


class Manager:
    """
    A class to manage all users

    Methods
    .......
    add_user(user_id, username):
        Adds a user instance to the users dictionary
    
    get_user(user_id):
        Returns the instance of a user based on their id

    list_aquariums:
        lists the aquariums owned by the user. this method
        is more for debugging
    """
    users: Dict[int, User] = {}

    @staticmethod
    def add_user(user_id: int, username: str) -> bool:
        if user_id in Manager.users:
            return False

        new_user = User(username, user_id, 100)
        Manager.users[user_id] = new_user
        return True

    @staticmethod
    def get_user(user_id: int):
        user = Manager.users.get(user_id)
        if user:
            return user
        else:
            print(f"User {user_id} not found.")
            return None

    @staticmethod
    def list_aquariums(user_id: int):
        user = Manager.users.get(user_id)
        if user:
            print(vars(user.aquarium))
        else:
            print(f"User {user_id} not found.")
