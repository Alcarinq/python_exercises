# 4.1
print("\n4.1")
pizza_types = ["American", "Mexican", "Polish"]

for pizza in pizza_types:
    print(pizza)

for pizza in pizza_types:
    print(f"Lubie pizze: {pizza}")
print("Pizza!")

# 4.2
animals = ["pies", "kot"]
for animal in animals:
    print(f"{animal} to fajne zwierze")
print("Ale wszystkie sa fajne!")

# 4.3
print("\n4.3")
numbers = list(range(1, 21))
print(numbers)

# 4.4
print("\n4.4")
numbers_milion = list(range(1, 1_000_001))
print(numbers_milion)

# 4.5
print("\n4.5")
print(min(numbers_milion))
print(max(numbers_milion))
print(sum(numbers_milion))

# 4.6
print("\n4.6")
numbers_2 = list(range(1, 21, 2))
for number in numbers_2:
    print(number)

# 4.7
print("\n4.7")
numbers_3 = []
for number in list(range(3, 31)):
    temp = number**3
    numbers_3.append(temp)
    print(temp)

# 4.8
print("\n4.8")
numbers_4 = [1**3, 2**3, 3**3, 4**3, 5**3, 6**3, 7**3, 8**3, 9**3, 10**3]
for number in numbers_4:
    print(number)

# 4.9
print("\n4.9")
szescian = [number**3 for number in list(range(1, 11))]
print(szescian)

# 4.10
print("\n4.10")
animals = ["Pies", "Kot", "Ptak", "Ryba", "Kon"]
print("Pierwsze 3 elementy listy to:")
for animal in animals[:3]:
    print(animal)
print("3 elementy w srodku listy to:")
for animal in animals[1:4]:
    print(animal)
print("3 elementy ostatnie listy to:")
for animal in animals[-3:]:
    print(animal)

# 4.11
print("\n4.11")
pizza_types = ["American", "Mexican", "Polish"]
friend_pizza_types = pizza_types[:]

pizza_types.append("Ukrainska")
friend_pizza_types.append("Brazylijska")

print("Moje ulubione pizze to:")
for pizza in pizza_types:
    print(pizza)

print("Ulubione pizze przyjaciela to:")
for pizza in friend_pizza_types:
    print(pizza)

# 4.12
print("\n4.12")

# 4.13
print("\n4.13")
food = ("a", "b", "c", "d", "e")

for f in food:
    print(f)

food = ("a", "b", "c", "f", "g")

for f in food:
    print(f)

# 4.14
print("\n4.14")

# 4.15
print("\n4.15")
