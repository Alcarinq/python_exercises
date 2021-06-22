# 3.1
print("\n3.1")
names = ["Bob", "Charls", "Ktos"]
print(names[0])
print(names[1])
print(names[2])

# 3.2
print("\n3.2")
print(f"Witaj: {names[0]}")
print(f"Witaj: {names[1]}")
print(f"Witaj: {names[2]}")

# 3.3
print("\n3.3")
super_list = ["Honda", "Toyota"]
print(f"Me like {super_list[0]} and {super_list[1]}")

# 3.4
print("\n3.4")
guests = ["Chuck", "Bruce", "Ken"]
print(f"Please come: {guests[0]}")
print(f"Please come: {guests[1]}")
print(f"Please come: {guests[2]}")

# 3.5
print("\n3.5")
print(f"Nie moze przyjsc: {guests[1]}")
guests[1] = "Bebe"
print(f"Please come: {guests[0]}")
print(f"Please come: {guests[1]}")
print(f"Please come: {guests[2]}")

# 3.6
print("\n3.6")
print("Znaleziono wiekszy stol")

guests.insert(0, "New1")
guests.insert(2, "New2")
guests.append("New3")

print(f"Please come: {guests[0]}")
print(f"Please come: {guests[1]}")
print(f"Please come: {guests[2]}")
print(f"Please come: {guests[3]}")
print(f"Please come: {guests[4]}")
print(f"Please come: {guests[5]}")

# 3.7
print("\n3.7")
print("Niestety moga przyjsc tylko 2 dodatkowe osoby")

print(f"Niestety: {guests.pop(0)} nie moze przyjsc")
print(f"Niestety: {guests.pop(0)} nie moze przyjsc")
print(f"Niestety: {guests.pop(0)} nie moze przyjsc")
print(f"Niestety: {guests.pop(0)} nie moze przyjsc")

print(f"Zapraszam na obiad: {guests[0]}")
print(f"Zapraszam na obiad: {guests[1]}")

del guests[0]
del guests[0]

print(f"Lista powinna byc pusta'{guests}'")

# 3.8
print("\n3.8")
places = ["B", "C", "A", "E", "D"]

print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)

print(len(places))

print(f"Pierwsze 3 elementy listy to: {places[:3]}")
print(f"3 elementy w srodku listy to: {places[1:4]}")
print(f"3 ostatnie elementy listy to: {places[-3:]}")

friend_places = places[:]
places.append("F")
friend_places.append("FF")

print("Moje:")
for place in places:
    print(place)

print("Friend:")
for place in friend_places:
    print(place)

new_places = [f"{place}x" for place in places]
print(new_places)

# 3.9
print("\n3.9")
print(len(places))

# 3.10
print("\n3.10")

# 3.11
print("\n3.11")
