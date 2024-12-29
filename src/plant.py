valid_plants = [
    "java_fern"
    "java_moss",
    "anubias",

]

class Plant:
    def __init__(self, species):
        if species not in valid_plants:
            print("Invalid species")
        