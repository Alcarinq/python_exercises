from bisect import bisect_left
from random import randint
import timeit

size = 10**5
iterations = 1000

data = list(range(size))
print(data)

to_lookup = [randint(0, size) for _ in range(iterations)]


def search_linear(data, to_lookup):
    for index in to_lookup:
        data.index(index)


def search_bisect(data, to_lookup):
    for index in to_lookup:
        bisect_left(data, index)

baseline = timeit.timeit(
    stmt='search_linear(data, to_lookup)',
    globals=globals(),
    number=10
)
print(f'Wyszukiwanie linear trwalo {baseline:.6f}')

biseline = timeit.timeit(
    stmt='search_bisect(data, to_lookup)',
    globals=globals(),
    number=10
)
print(f'Wyszukiwanie linear trwalo {biseline:.6f}')
