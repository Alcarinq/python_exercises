# 6.1
print("\n6.1")
person = {
    'first_name': 'Jan',
    'last_name': 'Kowalski',
    'age': 18,
    'city': 'Rzeszow',
}

print(f"Dane osoby to: Imie {person['first_name']}, Nazwisko {person['last_name']}, Wiek: {person['age']}, "
      f"Miasto: {person['city']}")

# 6.2
print("\n6.2")
favourite_numbers = {
    'jan': 1,
    'dawid': 2,
    'michal': 3,
    'marcin': 4,
    'maciek': 5,
}
for key, value in favourite_numbers.items():
    print(f"Ulubiona liczba {key} to {value}")

# 6.3
print("\n6.3")
glossary = {
    'dict': 'slownik',
    'tuple': 'krotka',
    'list': 'lista',
    'for': 'petla',
    'if': 'jesli',
}
for key, value in glossary.items():
    print(f"{key.title()} to znaczy: {value.title()}")

# 6.4
print("\n6.4")

glossary['test1'] = 'test1'
glossary['test2'] = 'test2'
glossary['test3'] = 'test3'
glossary['test4'] = 'test4'
glossary['test5'] = 'test5'

for key, value in glossary.items():
    print(f"{key.title()} to znaczy: {value.title()}")

# 6.5
print("\n6.5")
rivers = {
    'nil': 'egipt',
    'wisla': 'polska',
    'dunaj': 'rosja',
}

for k, v in rivers.items():
    print(f"{k.title()} przeplywa przez {v.title()}")

print("Wszystkie rzeki to:")
for river in rivers.keys():
    print(river)

print("Wszystkie panstwa to:")
for country in rivers.values():
    print(country)

# 6.6
print("\n6.6")
favourite_languages = {
    'jan': 'c',
    'dawid': 'python',
    'michal': 'java',
    'marcin': 'ruby',
    'maciek': 'java script',
}

should_vote = ['jan', 'edyta', 'maciek']

for person in should_vote:
    if person not in favourite_languages:
        print(f"Powinienes zaglosowac: {person}")
    else:
        print(f"Dziekujemy za udzial w ankiecie: {person}")

# 6.7
print("\n6.7")
person1 = {
    'first_name': 'Jan',
    'last_name': 'Kowalski',
    'age': 18,
    'city': 'Rzeszow',
}

person2 = {
    'first_name': 'Michal',
    'last_name': 'Skupien',
    'age': 23,
    'city': 'Wroclaw',
}

person3 = {
    'first_name': 'Maciej',
    'last_name': 'Kot',
    'age': 43,
    'city': 'Rzym',
}

people = [person1, person2, person3]

for p in people:
    print(f"Imie: {p['first_name'].title()}, Nazwisko: {p['last_name'].title()}, "
          f"Wiek: {p['age']}, Miasto: {p['city'].title()}")

# 6.8
print("\n6.8")
pies = {
    'burek': 'maciej',
    'azor': 'michal',
}

kot = {
    'miau': 'dawid',
    'mrr': 'andrzej',
}

pets = [pies, kot]

for p in pets:
    for k, v in p.items():
        print(f"Wlascicielem {k.title()} jest {v.title()} ")

# 6.9
print("\n6.9")
favourite_places = {
    'michal': ['rzym', 'morze', 'dom'],
    'maciek': ['lizbona', 'rzeka', 'miasto'],
    'adam': ['polska', 'piasek', 'plaza']
}

for k,v in favourite_places.items():
    print(f"Ulubione miejsca {k.title()} to:")
    for place in v:
        print(place)

# 6.10
print("\n6.10")
favourite_numbers = {
    'jan': [1, 2, 3],
    'dawid': [2],
    'michal': [3, 5, 7],
    'marcin': [4],
    'maciek': [5],
}
for key, value in favourite_numbers.items():
    print(f"Ulubione liczby {key} to:")
    for number in value:
        print(number)

# 6.11
print("\n6.11")
cities = {
    'rzym': {'country': 'wlochy', 'population': 1231854, 'fact': '1'},
    'wroclaw':  {'country': 'polska', 'population': 3314244, 'fact': '2'},
    'rzeszow':  {'country': 'polska', 'population': 54465, 'fact': '3'}
}

for city_name, data in cities.items():
    print(f"Miasto: {city_name.title()}, szczegoly: kraj: {data['country'].title()},"
          f" populacja: {data['population']}, fakt: {data['fact'].title()}")

# 6.12
print("\n6.12")
