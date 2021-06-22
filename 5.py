# 5.1
print("\n5.1")
name_1 = "subaru"
name_2 = "bmw"

print(name_1 == name_2)
print(name_1 != name_2)

# 5.2
print("\n5.2")

print(name_1.lower() == "BMW")
print(name_2.upper() == "BMW")

print("\n")
print(2 > 1)
print(1 < 2)
print(2 >= 1)
print(1 <= 2)

print("\n")
print(name_1 == "subaru" and name_2 == "bmw")
print(name_1 == "subaru" or name_2 == "bmw")

print("\n")
cars = ["subaru", "toyota"]
print(name_1 in cars)
print(name_2 in cars)

print("\n")
print(name_2 not in cars)
print("audi" not in cars)

# 5.3
print("\n5.3")
alien_color = 'zielony'

if alien_color == 'zielony':
    print("Zarobiles 5 punktow")

if alien_color == 'czerwony':
    print("Czerwony")

# 5.4
print("\n5.4")
alien_color = 'zielony'
if alien_color == 'zielony':
    print("Zarobiles 5 punktow")
else:
    print("Zarobiles 10 punktow")

alien_color = 'czerwony'
if alien_color == 'zielony':
    print("Zarobiles 5 punktow")
else:
    print("Zarobiles 10 punktow")

# 5.5
print("\n5.5")
alien_color = 'zielony'
if alien_color == 'zielony':
    print("Zarobiles 5 punktow")
elif alien_color == "zolty":
    print("Zarobiles 10 punktow")
elif alien_color == "czerwony":
    print("Zarobiles 15 punktow")

alien_color = 'zolty'
if alien_color == 'zielony':
    print("Zarobiles 5 punktow")
elif alien_color == "zolty":
    print("Zarobiles 10 punktow")
elif alien_color == "czerwony":
    print("Zarobiles 15 punktow")

alien_color = 'czerwony'
if alien_color == 'zielony':
    print("Zarobiles 5 punktow")
elif alien_color == "zolty":
    print("Zarobiles 10 punktow")
elif alien_color == "czerwony":
    print("Zarobiles 15 punktow")

# 5.6
print("\n5.6")
age = 13
if age < 2:
    print("Jestes niemowleciem")
elif 2 <= age < 4:
    print("Jestes dzieckiem, ktore uczy sie chodzic")
elif 4 <= age < 13:
    print("Jestes dzieckiem")
elif 13 <= age < 20:
    print("Jestes nastolatkiem")
elif 20 <= age < 65:
    print("Jestes doroslym")
elif 65 <= age:
    print("Jestes seniorem")

# 5.7
print("\n5.7")
favourite_fruits = ["banan", "jablko", "kiwi"]
if "kiwi" in favourite_fruits:
    print("Jest kiwi!")
if "jablko" in favourite_fruits:
    print("Jest jablko")
if "wisnia" in favourite_fruits:
    print("Jest wisnia")
if "banan" in favourite_fruits:
    print("Jest banan")
if "brzoskwinia" in favourite_fruits:
    print("Jest brzoskwinia")

# 5.8
print("\n5.8")
users = ["user1", "user2", "user3", "user4", "admin"]
for user in users:
    if user == "admin":
        print(f"Witaj {user}, czy chcesz kogos zbanowac?")
    else:
        print(f"Witaj {user}, Dziekujemy za logowanie!")

# 5.9
print("\n5.9")
users = ["user1", "user2", "user3", "user4", "admin"]
if not users:
    print("musimy znalezc jakich uzytkownikow!")
else:
    for user in users:
        if user == "admin":
            print(f"Witaj {user}, czy chcesz kogos zbanowac?")
        else:
            print(f"Witaj {user}, Dziekujemy za logowanie!")

users.clear()

if not users:
    print("musimy znalezc jakich uzytkownikow!")
else:
    for user in users:
        if user == "admin":
            print(f"Witaj {user}, czy chcesz kogos zbanowac?")
        else:
            print(f"Witaj {user}, Dziekujemy za logowanie!")

# 5.10
print("\n5.10")
current_users = ["user1", "user2", "user3", "user4", "Janek"]
new_users = ["user5", "user6", "Janek", "janek", "JANEK"]

for user in new_users:
    if user.lower() in [current_user.lower() for current_user in current_users]:
        print(f"Uzyj innej nazwy! {user} jest juz zajeta!")
    else:
        print(f"Mozna uzyc tej nazwy: {user}")

# 5.11
print("\n5.11")
numbers = list(range(1, 10))
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")

# 5.12
print("\n5.12")

# 5.13
print("\n5.13")
