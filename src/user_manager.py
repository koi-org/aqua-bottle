from user import User
from typing import Set

class UserManager:
    users: Set[User] = set()

    @staticmethod
    def add_user(user: User):
        if user in UserManager.users:
            return False
        UserManager.users.add(user)
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