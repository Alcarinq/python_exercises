# 10.1
print("\n10.1")

filepath = 'words.txt'
words = []
with open(filepath) as file:
    print("Caly plik")
    print(file.read())

with open(filepath) as file:
    print("Linia po linii")
    for line in file:
        print(line.strip())

with open(filepath) as file:
    print("Na Liscie")
    words = file.readlines()

for word in words:
    print(word.strip())

# 10.2
print("\n10.2")
with open(filepath) as file:
    for line in file:
        print(line.strip().replace('Ucze', 'Nie ucze'))

# 10.3
print("\n10.3")
file_name = 'guest.txt'
name = input("Prosze podac imie: ")
with open(file_name, 'w') as file_obj:
    file_obj.write(name)

# 10.4
print("\n10.4")
file_name = 'guest_book.txt'
active = True
with open(file_name, 'a') as file_obj:
    while active:
        name = input("Prosze podac imie: (wpisz N, zeby przerwac)")
        if name == 'N':
            active = False
            break
        file_obj.write(f"{name}\n")

# 10.5
print("\n10.5")
file_name = 'answers.txt'
active = True
with open(file_name, 'a') as file_obj:
    while active:
        answer = input("Dlaczego lubisz programowac? : (wpisz N, zeby przerwac) ")
        if answer == 'N':
            active = False
            break
        file_obj.write(f"{answer}\n")

# 10.6
print("\n10.6")


def calc():
    num_1 = input("Podaj liczbe 1: ")
    num_2 = input("Podaj liczbe 2: ")
    try:
        suma = int(num_1) + int(num_2)
    except ValueError:
        print("Podaj liczbe a nie litere!")
    else:
        print(f"Suma liczb to: {suma}")


calc()
calc()

# 10.7
print("\n10.7")
active = True
print("Wcisnij N zeby przerwac")
while active:
    num_1 = input("Podaj liczbe 1: ")
    num_2 = input("Podaj liczbe 2: ")
    if num_1 == 'N'or num_2 == 'N':
        active = False
        break
    try:
        suma = int(num_1) + int(num_2)
    except ValueError:
        print("Podaj liczbe a nie litere!")
    else:
        print(f"Suma liczb to: {suma}")

# 10.8
print("\n10.8")


def open_and_read_file(filename):
    try:
        with open(filename) as file_obj:
            print(file_obj.read().strip())
    except FileNotFoundError:
        print(f"Nie znaleziono pliku {filename}!")


open_and_read_file('cats.txt')
open_and_read_file('dogs.txt')
open_and_read_file('cows.txt')


# 10.9
print("\n10.9")


def open_and_read_file(filename):
    try:
        with open(filename) as file_obj:
            print(file_obj.read().strip())
    except FileNotFoundError:
        pass


open_and_read_file('cats.txt')
open_and_read_file('dogs.txt')
open_and_read_file('cows.txt')


# 10.10
print("\n10.10")
file_1 = '65650-0.txt'
with open(file_1, encoding='UTF-8') as file1:
    lines = file1.read()
    print(lines.lower().count('boy'))
    print(lines.lower().count('boy '))