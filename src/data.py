import json
import os
import shutil
from filelock import FileLock

def ensure_dict(value):
    if not isinstance(value, dict):
        raise TypeError("not a dict :(")
    return value


def read_data(user_id):
    user_file = f"./data/{user_id}.json"
    lock_file = f"./{user_file}.lock.read"
    lock = FileLock(lock_file)

    with lock:
        try:
            with open(user_file, 'r') as f:
                user_data = json.load(f)

            ensure_dict(user_data)
            return user_data

        except FileNotFoundError:
            return {}


def write_data(user_id, new_data):
    user_file = f"./data/{user_id}.json"
    temp_file = f"./data/{user_id}.temp"
    lock_file = f"./data/{user_id}.lock.write"
    lock = FileLock(lock_file)

    with lock:
        data = read_data(user_id)
        ensure_dict(new_data)
        data.update(new_data)

        with open(temp_file, 'w') as f:
            json.dump(data, f, indent=4)

        shutil.move(temp_file, user_file)


def test():
    id = '12345'
    person = {
        "first_name": "John",
        "last_name": "Doe",
        "age": 30,
        "is_employed": True,
        "skills": ["Python", "JavaScript", "SQL"],
        "address": {
            "street": "123 Main St",
            "city": "Springfield",
            "zip_code": "12345"
        }
    }
    not_a_person = "person"

    print("#1")
    my_data = read_data(user_id=id)
    print(my_data)

    print("#2")
    write_data(user_id=id, new_data=person)
    my_data = read_data(user_id=id)
    print(my_data)

    print("#3")
    person["first_name"] = "Steve"
    person["age"] = 50
    write_data(user_id=id, new_data=person)
    my_data = read_data(user_id=id)
    print(my_data)

    print("#4")
    write_data(user_id=id, new_data=not_a_person)
    my_data = read_data(user_id=id)
    print(my_data)


test()