class User:
    def __init__(self, name: str, id: int, balance: float):
        self.name = name
        self.id = id
        self.aquariums = []
        self.balance = balance

    def __str__(self):
        return f"{self.name} ({self.balance})"
