from printing_functions import print_models, show_completed_models

# 8.1
print("\n8.1")


def display_messages():
    print("Uczymy sie funkcji")


display_messages()

# 8.2
print("\n8.2")


def favourite_book(title):
    print(f"Jedna z moich ulubionych ksiazek jest {title.title()}")


favourite_book('alicja w krainie czarow')

# 8.3
print("\n8.3")


def make_shirt(size, text):
    print(f"Koszulka z rozmiarem {size} zostanie wydrukowana z textem: {text}")


make_shirt('S', 'Pokemon')
make_shirt(size='L', text='Jack')

# 8.4
print("\n8.4")


def make_shirt(size='L', text='Lubie Pythona'):
    print(f"Koszulka z rozmiarem {size} zostanie wydrukowana z textem: {text}")


make_shirt('L')
make_shirt('S')
make_shirt('M', 'Jack')
make_shirt(size='S', text='Jack2')

# 8.5
print("\n8.5")


def describe_city(city_name, country_name='Polska'):
    print(f"{city_name.title()} lezy w {country_name.title()}")


describe_city('Wroclaw')
describe_city('Rzeszow')
describe_city('Rzym', 'Wlochy')

# 8.6
print("\n8.6")


def city_country(city_name, country_name):
    return f"{city_name.title()}, {country_name.title()}"


print(city_country('Rzym', 'Wlochy'))
print(city_country('Wroclaw', 'Polska'))
print(city_country('Berlin', 'Niemcy'))

# 8.7
print("\n8.7")


def make_album(band_name, title_album, track_number=None):
    album = {'band_name': band_name, 'title_album': title_album}
    if track_number:
        album['track_number'] = track_number
    return album


print(make_album('Pezet', 'Noc'))
print(make_album('Peja', 'Dzien'))
print(make_album('Ktos', 'Poludnie'))
print(make_album('Jeszzcze ktos inny', 'Polnoc', 12))

# 8.8
print("\n8.8")
# active = True
active = False
albums = []
while active:
    bn = input('Podaj nazwe teamu: ')
    ta = input('Podaj tytul albumu: ')
    tn = input('Podaj liczbe utworow (opcjonalne - jesli nie chcesz podac wcisnij enter): ')
    albums.append(make_album(bn, ta, tn))

    if input('Chcesz podac nastepny? Y/N ') == 'N':
        active = False

print(albums)

# 8.9
print("\n8.9")
comms = ['STOP', 'JEDZ', 'COSTAM']


def show_messages(msgs):
    for msg in msgs:
        print(msg)


show_messages(comms)

# 8.10
print("\n8.10")
comms = ['STOP', 'JEDZ', 'COSTAM']
sent_messages = []


def show_messages(msgs, name=''):
    print(f"Printuje : {name}")
    for msg in msgs:
        print(msg)


def send_messages(msgs):
    show_messages(msgs)
    while msgs:
        item = msgs.pop()
        sent_messages.append(item)


send_messages(comms)
show_messages(comms, 'comms')
show_messages(sent_messages, 'sent_messages')

# 8.11
print("\n8.11")
comms = ['STOP', 'JEDZ', 'COSTAM']
sent_messages = []

send_messages(comms[:])
show_messages(comms, 'comms')
show_messages(sent_messages, 'sent_messages')

# 8.12
print("\n8.12")


def build_sandwitch(*toppings):
    print('Bedziemy robic kanapke z takimi skladnikami:')
    for topping in toppings:
        print(topping)


build_sandwitch('ser')
build_sandwitch('ser', 'mieso')
build_sandwitch('ser', 'mieso', 'ogorek')

# 8.13
print("\n8.13")


def build_profile(first, last, **user_info):
    """Budowa uzytkownia"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('M', 'M', location='Rzeszow', lang='Python', exp='mid')
print(user_profile)

# 8.14
print("\n8.14")


def make_car(company, model, **car_info):
    """Budowanie samochodu"""
    car_info['company'] = company
    car_info['model'] = model
    return car_info


car = make_car('subaru', 'impreza', color='black', tow_package=True)

print(car)

# 8.15
print("\n8.15")
unprinted_designs = ['etui', 'drzewo', 'wieza']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# 8.16
print("\n8.16")
# import printing_functions
unprinted_designs = ['etui', 'drzewo', 'wieza']
completed_models = []

# printing_functions.print_models(unprinted_designs, completed_models)
# printing_functions. show_completed_models(completed_models)

# from printing_functions import print_models, show_completed_models
# from printing_functions import print_models as pm, show_completed_models as scm
# import printing_functions as pf
# from printing_functions import *

# 8.17
print("\n8.17")
