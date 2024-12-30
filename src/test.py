from user import User
from manager import UserManager
from aquarium import Aquarium


# Use User and UserManager together here
def test_add_user():
    user = User(name="Test User", id=1, balance=100.0)
    UserManager.add_user(user)
    assert user in UserManager.users


def test_user_exists():
    user = User(name="Test User", id=2, balance=100.0)
    UserManager.add_user(user)
    assert UserManager.user_exists(2)


def create_aquarium():
    user = User(name="Test User", id=3, balance=100.0)
    UserManager.add_user(user)
    aquarium = Aquarium(user, channel_id=10)
    new_aquarium = Aquarium(user, channel_id=11)

    UserManager.list_aquariums(user)


create_aquarium()
