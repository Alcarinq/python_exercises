class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.password = '***'
        self.login_attempts = 0

    def describe_user(self):
        print(f"Uzytkownik {self.first_name} {self.last_name} ma haslo {self.password}")

    def greet_user(self):
        print(f"Witaj {self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0