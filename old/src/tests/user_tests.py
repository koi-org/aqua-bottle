from classes.manager import Manager


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
    assert user is Manager.users[3]
    assert user.name == "Charlie"
    assert user.balance == 100

    user = Manager.get_user(user_id=4)
    assert user is Manager.users[4]
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


def test_retrieve_user_when_no_users():
    Manager.users.clear()
    assert Manager.get_user(1) is None


def test_retrieve_user_after_clear():
    Manager.add_user(user_id=1, username="TestUser")
    Manager.users.clear()
    assert Manager.get_user(1) is None


def test_add_users_with_same_username():
    user1 = Manager.add_user(user_id=6, username="DuplicateName")
    user2 = Manager.add_user(user_id=7, username="DuplicateName")

    assert user1 is True
    assert user2 is True
    assert Manager.get_user(6).name == "DuplicateName"
    assert Manager.get_user(7).name == "DuplicateName"


def test_add_user_after_removal():
    Manager.add_user(user_id=8, username="RemovableUser")
    del Manager.users[8]  # Simulate removing the user
    assert Manager.get_user(8) is None  # Ensure the user was removed

    result = Manager.add_user(user_id=8, username="NewUser")
    assert result is True  # Should allow adding a new user with the same ID
    assert Manager.get_user(8).name == "NewUser"


def test_add_large_number_of_users():
    Manager.users.clear()
    num_users = 10000
    for user_id in range(num_users):
        assert Manager.add_user(user_id=user_id, username=f"User{user_id}") is True

    assert len(Manager.users) == num_users
