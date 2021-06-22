# 7.1
print("\n7.1")
car = input("Jakiej marki chcialbys samochod?")
print(f"Chwileczke, sprawdze czy mamy {car}")

# 7.2
print("\n7.2")
rest = input("Na ile osob chcialbys stolik?")
if int(rest) > 8:
    print("Zaczekaj na stolik")
else:
    print("Stolik gotowy")

# 7.3
print("\n7.3")
number = input("Podaj liczbe")
if int(number) % 10 == 0:
    print("Liczba jest wielokrotnoscia 10")
else:
    print("Liczba nie jest wielokrotnoscia 10")

# 7.4
print("\n7.4")
print("Podaj dodatki do pizzy, wpisanie koniec konczy petle.")
flag = True
while flag:
    topping = input("Podaj dodatek:")
    if topping != 'koniec':
        print(topping)
    else:
        flag = False

# 7.5
print("\n7.5")
print("Podaj wiek, zeby wyswietlic cene biletu, wpisanie koniec konczy petle.")

active = True
while active:
    age = input("Podaj wiek")
    if age.isnumeric():
        age = int(age)
        if age < 3:
            print("Bilet bezplatny")
        elif 3 <= age <= 12:
            print("Bilet kosztuje 10zl")
        elif age > 12:
            print("Bilet kosztuje 15zl")
    elif age == 'koniec':
        print("Wpisano 'koniec'")
        break
    else:
        active = False

# 7.6
print("\n7.6")

# 7.7
print("\n7.7")
#while True:
    #print("hehe")

# 7.8
print("\n7.8")
sandwitch_orders = ['kanapka1', 'kanapka2', 'kanapka3']
finished_sandwitches = []

while sandwitch_orders:
    sandwitch = sandwitch_orders.pop()
    print(f"Przygotowano kanapke {sandwitch}")
    finished_sandwitches.append(sandwitch)

print(f"Lista przygotowanych kanapek: {finished_sandwitches}")

# 7.9
print("\n7.9")
sandwitch_orders = ['kanapka1', 'kanapka2', 'kanapka3', 'kanapka2', 'kanapka2']
finished_sandwitches = []

print("Skonczyly sie kanapka2")

while 'kanapka2' in sandwitch_orders:
    sandwitch_orders.remove('kanapka2')

while sandwitch_orders:
    sandwitch = sandwitch_orders.pop()
    print(f"Przygotowano kanapke {sandwitch}")
    finished_sandwitches.append(sandwitch)

print(f"Lista przygotowanych kanapek: {finished_sandwitches}")

# 7.10
print("\n7.10")

active = True
results = {}
while active:
    name = input("Podaj imie: ")
    place = input("Jezeli moglbys odwiedzic jedno miejsce to gdzie bys pojechal?: ")
    results[name] = place
    question = input("Chcesz kontynuowac? tak/nie: ")
    if question == 'nie':
        active = False

for key, value in results.items():
    print(f"{key.title()} chcialby pojechac do: {value.title()}")



