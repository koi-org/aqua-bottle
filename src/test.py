from user import User
from user_manager import UserManager

# Use User and UserManager together here
user1 = User(name="Son Doumeg", id=59, aquarium=[], balance=999)


UserManager.add_user(user1)
user_exists = UserManager.user_exists(user1.id)
print(f"Does user {user1.name} exist? {user_exists}")


print("Current users:")
for user in UserManager.users:
    print(user)