import json
numbers = [2, 3, 4, 5, 6]
read_numbers = []
filename = 'numbers.json'
with open(filename, 'w') as file:
    json.dump(numbers, file)

with open(filename) as file:
    read_numbers = json.load(file)

print(read_numbers)

# 10.11
print("\n10.11")
fav_number_filename = 'fav_number.json'
number = int(input("Podaj ulubiona liczbe: "))
with open(fav_number_filename, 'w') as file:
    json.dump(number, file)

with open(fav_number_filename) as file:
    fav_number = json.load(file)
print(f"Twoja ulubiona liczba to: {fav_number}")


# 10.12
print("\n10.12")
fav_number_filename2 = 'fav_number2.json'
try:
    with open(fav_number_filename2) as file:
        fav_number2 = json.load(file)
except FileNotFoundError:
    number = int(input("Podaj ulubiona liczbe: "))
    with open(fav_number_filename2, 'w') as file:
        json.dump(number, file)
    print(f"Zapisano liczbe: {number}")
else:
    print(f"Twoja ulubiona liczba to: {fav_number2}")

# 10.13
print("\n10.13")

