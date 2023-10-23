"""
Перед вами список целых чисел. Ваша задача в этой миссии – продублировать (..., 🍩, ... --> ..., 🍩, 🍩, ...)
все нули в данном списке (думайте о пончиках ;-P) и вернуть в виде любого итерируемого объекта. Посмотрим на пример:

[1, 0, 2, 0] -> [1, 0, 0, 2, 0, 0]

Входные данные: Список целых чисел.

Выходные данные: Список или другой итерируемый объект (кортеж, генератор, итератор) из целых чисел.
"""
from collections.abc import Iterable


def duplicate_zeros(donuts):
    result = []
    for number in donuts:
        result.append(number)
        if number == 0:
            result.append(number)
    # your code here
    return result


print("Example:")
print(list(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0])))

# These "asserts" are used for self-checking
assert list(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0])) == [
    1,
    0,
    0,
    2,
    3,
    0,
    0,
    4,
    5,
    0,
    0,
]
assert list(duplicate_zeros([0, 0, 0, 0])) == [0, 0, 0, 0, 0, 0, 0, 0]
assert list(duplicate_zeros([100, 10, 0, 101, 1000])) == [100, 10, 0, 0, 101, 1000]

print("The mission is done! Click 'Check Solution' to earn rewards!")
