import json
import os
from filelock import FileLock
from pathlib import Path

def ensure_dict(value):
    if not isinstance(value, dict):
        raise TypeError("not a dict :(")
    return value

def read_data(user_id):
    user_file = f"./data/{user_id}.json"
    lock_file = Path(f"{user_file}.lock.read")
    lock = FileLock(lock_file)

    with lock:
        try:
            with open(user_file, 'r') as f:
                user_data = json.load(f)

            ensure_dict(user_data)
            return user_data

        except FileNotFoundError:
            print(f"file not found: {user_file}")
            return {}

        finally:
            if lock_file.exists():
                lock_file.unlink()


user_id = '12345'
user_data = read_data(user_id)