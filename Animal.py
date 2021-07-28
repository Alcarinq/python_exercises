class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hungry = True

    def __repr__(self):
        return f"Animal(name: {self.name}, age: {self.age}, hungry: {self.hungry})"

    def is_food_needed(self):
        if self.hungry:
            print(f"Animal {self.name} need food!")
            return True
        else:
            print(f"Animal {self.name} doesnt need food!")
            return False

    def feed_animal(self):
        self.hungry = False
        print(f"Animal {self.name} has been feed!")

