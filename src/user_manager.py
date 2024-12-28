from user import User

class UserManager:
    users: User = []

    @staticmethod
    def add_user(user):
        if not isinstance(user, User):
            raise TypeError("not a user :()")

        if UserManager.user_exists(user.user_id):
            raise ValueError("user already exists")

        UserManager.users.append(user)
