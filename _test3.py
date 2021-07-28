# iteracja enumerate, bez inkdeksowania
print('\n 1 \n')
lody = ['waniliowe', 'kokosowe', 'czekoladowe', 'cytrynowe']

for i in range(len(lody)):
    print(f"{i + 1}: lody {lody[i]} sa swietne")

for i, flavour in enumerate(lody, 1):
    print(f"{i}: lody {flavour} sa swietne")


# zip do przetwarzania iteratorow
print('\n 2 \n')
icecreams = ['waniliowe', 'kokosowe', 'czekoladowe', 'cytrynowe']
lenght_ice_cream = [len(i) for i in icecreams]

for icecream, count in zip(icecreams, lenght_ice_cream):
    print(f"{icecream} ma dlugosc {count}")

# operator przypisania walrus :=
print('\n 3 \n')

if (count := len(icecreams)) > 4:
    print(f'Jestes prawdziwym smakoszem lodow, lubisz {count} typow')
else:
    print(f'Srednio lubisz lody, lubisz tylko {count} typow')