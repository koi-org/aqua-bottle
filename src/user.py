class User:
    def __init__(self, name: str, id: int, aquarium: list, balance: float):
        self.name = name
        self.id = id
        self.aquarium = aquarium
        self.balance = balance

        if self.exists():
            raise ValueError("User already exists")
        else:
            User.user_data.append(self)

    def __str__(self):
        return f"{self.name} (${self.balance})"

    def exists(self):
        for user in User.user_data:
            if user.id == self.id:
                return True
            return False


# user1 = User(name="Son Doumeg", id = 59, aquarium=None, balance=999)
# print(user1)
# user2 = User(name="Son Doumeg", id = 59, aquarium=None, balance=999)
# print(user2)

# print("hi")