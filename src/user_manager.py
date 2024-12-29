from user import User
from typing import Set

class UserManager:
    users: Set[User] = set()

    @staticmethod
    def add_user(user):
        if user in UserManager.users:
            print("user already exists")
        UserManager.users.add(user)

    @staticmethod
    def get_user(user_id):
        for user in UserManager.users:
            if user.id == user_id:
                return user

    @staticmethod
    def list_aquariums(user):
        for user in UserManager.users:
            for aquarium in user.aquariums:
                print(vars(aquarium))