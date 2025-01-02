from classes.user import User
from classes.manager import Manager
from classes.aquarium import Aquarium


# Use User and Manager together here
def test_add_user():
    user = User(name="Test User", id=1, balance=100.0)
    Manager.add_user(user)
    assert user in Manager.users


def test_user_exists():
    user = User(name="Test User", id=2, balance=100.0)
    Manager.add_user(user)
    assert Manager.user_exists(2)


def create_aquarium():
    user = User(name="Test User", id=3, balance=100.0)
    Manager.add_user(user)
    aquarium = Aquarium(user, channel_id=10)
    new_aquarium = Aquarium(user, channel_id=11)

    Manager.list_aquariums(user)


create_aquarium()
