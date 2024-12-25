import json
import os
from filelock import FileLock
import shutil

def read_user_data(user_id):
    user_file = f"user_data_{user_id}.json"
    lock_file = f"{user_file}.lock"  # Lock file for user

    # Create a read lock
    lock = FileLock(lock_file + ".read")

    # Acquire the read lock
    with lock:
        try:
            with open(user_file, 'r') as f:
                user_data = json.load(f)
            return user_data
        except FileNotFoundError:
            return {}  # Return empty dict if user data does not exist

def write_user_data(user_id, new_data):
    user_file = f"user_data_{user_id}.json"
    temp_file = f"{user_file}.temp"
    lock_file = f"{user_file}.lock"  # Lock file for user

    # Create a write lock (exclusive)
    lock = FileLock(lock_file + ".write")

    # Acquire the write lock
    with lock:
        # Read the current user data
        user_data = read_user_data(user_id)

        # Update the data
        user_data.update(new_data)

        # Write the updated data to a temporary file
        with open(temp_file, 'w') as f:
            json.dump(user_data, f, indent=4)

        # Replace the original file with the temporary file atomically
        shutil.move(temp_file, user_file)

# Example usage:
user_id = '12345'

# Update the data (for example, adding a fish to the aquarium)
write_user_data(user_id, {'fish': ['goldfish', 'betta fish']})

# Read the updated data
user_data = read_user_data(user_id)
print(user_data)
