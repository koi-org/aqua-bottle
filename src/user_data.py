import json
import os
from filelock import FileLock
import shutil

def read_user_data(user_id):
    user_file = f"./data/{user_id}.json"
    lock_file = f"{user_file}.lock"

    lock = FileLock(lock_file + ".read")
    with lock:
        try:
            with open(user_file, 'r') as f:
                user_data = json.load(f)
            return user_data
        except FileNotFoundError:
            print(f"file not found: {user_file}")
            return {}
