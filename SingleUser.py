from User import User


class Priviledges:
    def __init__(self, priviledges):
        self.priviledges = priviledges

    def show_priviledges(self):
        for p in self.priviledges:
            print(f"Uzytkownik moze {p}")


class Admin(User):
    def __init__(self, first_name, last_name):
        self.priviledges = Priviledges(["moze dodawac", "moze usuwac"])
        super().__init__(first_name, last_name)
