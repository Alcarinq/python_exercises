# 9.1
print("\n9.1")


class Restaurant:
    open_hour = '8'
    close_hour = '16'

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restarurant(self):
        print(f"Restauracja {self.restaurant_name} serwuje {self.cuisine_type}")

    def open_restarurant(self):
        print(f"Restauracja pracuje w godzinach {self.open_hour}-{self.close_hour}")


restaurant = Restaurant('Long Phung', 'azjatyckie jedzenie')
restaurant.describe_restarurant()
restaurant.open_restarurant()

# 9.2
print("\n9.2")
res1 = Restaurant('Long Phung', 'azjatyckie jedzenie')
res2 = Restaurant('Ukrainska Chata', 'ukrainskie jedzenie')
res3 = Restaurant('Bistro Chata', 'polskie jedzenie')

res1.describe_restarurant()
res2.describe_restarurant()
res3.describe_restarurant()

# 9.3
print("\n9.3")


class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.password = '***'

    def describe_user(self):
        print(f"Uzytkownik {self.first_name} {self.last_name} ma haslo {self.password}")

    def greet_user(self):
        print(f"Witaj {self.first_name} {self.last_name}")


usr1 = User('Maciej', 'Kloss')
usr2 = User('Michal', 'Janosik')

usr1.describe_user()
usr1.greet_user()

usr2.describe_user()
usr2.greet_user()

# 9.4
print("\n9.4")


class Restaurant:
    open_hour = '8'
    close_hour = '16'

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restarurant(self):
        print(f"Restauracja {self.restaurant_name} serwuje {self.cuisine_type}")

    def open_restarurant(self):
        print(f"Restauracja pracuje w godzinach {self.open_hour}-{self.close_hour}")

    def served_clients(self):
        print(f"Oblsluzono {self.number_served} klientow")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, number_served):
        self.number_served += number_served


restaurant = Restaurant('Long Phung', 'azjatyckie jedzenie')
restaurant.served_clients()
restaurant.number_served = 12
restaurant.served_clients()
restaurant.set_number_served(20)
restaurant.served_clients()
restaurant.increment_number_served(2)
restaurant.served_clients()

# 9.5
print("\n9.5")


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


user = User('Maciej', 'Kloss')
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)

# 9.6
print("\n9.6")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, ice_cream_flavours):
        self.flavours = ice_cream_flavours
        super().__init__(restaurant_name, cuisine_type)

    def show_ice_creams(self):
        for f in self.flavours:
            print(f)


flavours = ['mietowe', 'malinowe', 'sorbet']
ice_cream_restaurant = IceCreamStand('Lodziarnia', 'lody', flavours)
ice_cream_restaurant.describe_restarurant()
ice_cream_restaurant.show_ice_creams()


# 9.7
print("\n9.7")


class Admin(User):
    def __init__(self, first_name, last_name, priviledges):
        self.priviledges = priviledges
        super().__init__(first_name, last_name)

    def show_priviledges(self):
        for p in self.priviledges:
            print(f"Uzytkownik moze {p}")


user_priviledges = ["moze dodawac", "moze usuwac"]
user_admin = Admin('Admin', 'Admin', user_priviledges)
user_admin.show_priviledges()

# 9.8
print("\n9.8")


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


user2_admin = Admin('Admin2', 'Admin2')
user2_admin.priviledges.show_priviledges()

# 9.9
print("\n9.9")


class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()

# 9.10
print("\n9.10")

# 9.11
print("\n9.11")

# 9.12
print("\n9.12")

# 9.13
print("\n9.13")
import random


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(f"Wyrzucono: {random.randint(1, self.sides)}")


die_6 = Die()
for number in range(10):
    die_6.roll_die()

print(f"\n")

die_10 = Die(10)
for number in range(10):
    die_10.roll_die()

print(f"\n")

die_20 = Die(20)
for number in range(10):
    die_20.roll_die()


# 9.14
print("\n9.14")
list_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A', 'B', 'C', 'D', 'E']
lucky_numbers = []
for number in range(4):
    lucky_numbers.append(random.choice(list_numbers))

print(f"W losowaniu wybrano takie liczby/numery jak:")
for lucky_number in lucky_numbers:
    print(lucky_number)


# 9.15
print("\n9.15")
my_ticket = ['4', '7', 'E', '0']
tries = {my_ticket[0]: 0, my_ticket[1]: 0, my_ticket[2]: 0, my_ticket[3]: 0}

for my_number in my_ticket:
    while random.choice(list_numbers) != my_number:
        tries[my_number] += 1

for k, v in tries.items():
    print(f"{k} losowano {v} razy, az zostalo wylosowane")


# 9.16
print("\n9.16")
