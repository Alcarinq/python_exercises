address = 'Lat temu osiemdziesiat i siedem...'


def index_words(text):
    if text:
        yield 0
    for index, letter in enumerate(text, 1):
        if letter == ' ':
            yield index


print(list(index_words(address)))


def child():
    for i in range(100):
        yield i

def slow():
    for i in child():
        yield i

def fast():
    yield from child()


print(' '.join(str(x) for x in list(slow())))
print(' '.join(str(x) for x in list(fast())))
