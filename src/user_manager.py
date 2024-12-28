from user import User

class UserManager:
    users: User = []

    @staticmethod
    def add_user(user):
        if not isinstance(user, User):
            raise TypeError("not a user :()")

        if UserManager.user_exists(user.id):
            raise ValueError("user already exists")

        UserManager.users.append(user)

    @staticmethod
    def user_exists(user_id):
        for user in UserManager.users:
            if user.id == user_id:
                return True
        return False
