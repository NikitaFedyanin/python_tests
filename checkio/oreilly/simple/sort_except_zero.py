"""
Sort the integers in sequence in sequence. But the position of zeros should not be changed.
"""
from collections.abc import Iterable


def except_zero(items: list[int]) -> Iterable[int]:
    indexes = []
    new_items = []
    for i, v in enumerate(items):
        if v == 0:
            indexes.append(i)
        else:
            new_items.append(v)
    new_items.sort()
    for i in indexes:
        new_items.insert(i, 0)

    return new_items


print("Example:")
print(list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])))

# These "asserts" are used for self-checking
assert list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
assert list(except_zero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
assert list(except_zero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
assert list(except_zero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]
assert list(except_zero([0, 0])) == [0, 0]

print("The mission is done! Click 'Check Solution' to earn rewards!")