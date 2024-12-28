from user import User

class UserManager:
    users = []

    @staticmethod
    def add_user(user):
        if not isinstance(user, User):
            raise TypeError("Not a User object")

        if UserManager.user_exists(user.id):
            raise ValueError("User already exists")

        UserManager.users.append(user)

    @staticmethod
    def user_exists(user_id):
        for user in UserManager.users:
            if user.id == user_id:
                return True
        return False

    @staticmethod
    def get_user(user_id):
        for user in UserManager.users:
            if user.id == user_id:
                return user
    
    @staticmethod
    def list_aquariums(user):
        for aquarium in user.aquariums:
            print(vars(aquarium))