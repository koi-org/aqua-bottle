from classes.user import User
from classes.manager import Manager
# from classes.aquarium import Aquarium


# Use User and Manager together here
def test_add_user():
    add_user = Manager.add_user(user_id=1, username="bob")
    assert add_user is True


def test_user_exists():
    user_id = 2
    new_user = Manager.add_user(username="Test User", user_id=user_id)
    assert new_user is True
    assert Manager.get_user(user_id)


def test_user_does_not_exist():
    invalid_id = 10
    assert Manager.get_user(invalid_id) is None
