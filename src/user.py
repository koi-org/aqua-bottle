class User:
    user_data = []

    def __init__(self, name: str, aquarium: list, balance: float):
        self.name = name
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
            if user.name == self.name and user.aquarium == self.aquarium and user.balance == self.balance:
                return True
            return False

    

user1 = User(name="Son Doumeg", aquarium=None, balance=999)
print(user1)