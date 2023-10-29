"""
В заданном списке последний элемент должен стать первым.
Пустой список или список с одним элементом должен оставаться неизменным
"""
from typing import Iterable


def replace_last(line: list) -> Iterable:
    if line:
        line = [line.pop(-1)] + line
    return line


print("Example:")
print(list(replace_last([2, 3, 4, 1])))

assert list(replace_last([2, 3, 4, 1])) == [1, 2, 3, 4]
assert list(replace_last([1, 2, 3, 4])) == [4, 1, 2, 3]
assert list(replace_last([1])) == [1]
assert list(replace_last([])) == []

print("The mission is done! Click 'Check Solution' to earn rewards!")