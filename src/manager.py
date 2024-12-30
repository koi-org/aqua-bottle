from user import User
from typing import Dict

# Manage all users here
manager: Dict[int, User] = {}

def add_user(user_id: int, username: str) -> bool:
    if user_id in manager:
        return False

    new_user = User(username, user_id, 100)
    manager[user_id] = new_user
    return True

def get_user(user_id: int):
    user = manager.get(user_id)
    if user:
        return user
    else:
        print(f"User {user_id} not found.")
        return None

def list_aquariums(user_id: int):
    user = manager.get(user_id)
    if user:
        print(vars(user.aquarium))
    else:
        print(f"User {user_id} not found.")
