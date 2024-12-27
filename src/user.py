class User:
    def __init__(self, name: str, aquarium: list, balance: float):
        self.name = name
        self.aquarium = aquarium
        self.balance = balance

    def __str__(self):
        return f"{self.name} (${self.balance})"


user1 = User(name="Son Doumeg", aquarium=None, balance=999)
print(user1)