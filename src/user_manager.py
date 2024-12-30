from user import User
from typing import Dict

class UserManager:
    users: Dict[int, User] = set()

    @staticmethod
    def add_user(user_id: int, username: str):
        if user_id in UserManager.users:
            return False

        new_user = User(username, user_id, 100)
        UserManager.users[user_id] = new_user
        return True

    @staticmethod
    def get_user(user_id: int):
        for user in UserManager.users:
            if user.id == user_id:
                return user

    @staticmethod
    def list_aquariums(user: User):
        for user in UserManager.users:
            for aquarium in user.aquariums:
                print(vars(aquarium))