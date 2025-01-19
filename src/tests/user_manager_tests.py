from classes.manager import Manager

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


def test_get_user_by_id():
    Manager.add_user(user_id=3, username="Charlie")
    Manager.add_user(user_id=4, username="Dave")

    user = Manager.get_user(user_id=3)
    assert user is not None
    assert user.name == "Charlie"
    assert user.balance == 100

    user = Manager.get_user(user_id=4)
    assert user is not None
    assert user.name == "Dave"
    assert user.balance == 100


def test_duplicate_users():
    Manager.users.clear()
    duplicate_user_id = 1
    user1 = Manager.add_user(user_id=duplicate_user_id, username="Lebron James")
    user2 = Manager.add_user(user_id=duplicate_user_id, username="Lebron James")
    user3 = Manager.add_user(user_id=duplicate_user_id, username="Michael Jordan")

    assert user1 is True
    assert user2 is False
    assert user3 is False

def test_negative_user_id():
    invalid_id = -1
    user1 = Manager.add_user(user_id=invalid_id, username="Russel Westbrook")
    assert user1 is False