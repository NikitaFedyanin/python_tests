"""
В данном списке первый элемент должен стать последним.
 Пустой список или список из одного элемента не должен измениться.
"""
from collections.abc import Iterable


def replace_first(items: list) -> Iterable:
    # your code here
    if not items or len(items) == 1:
        return items
    items.append(items.pop(0))
    return items


# These "asserts" are used for self-checking
print("Example:")
print(list(replace_first([1, 2, 3, 4])))

assert replace_first([1, 2, 3, 4]) == [2, 3, 4, 1]
assert replace_first([1]) == [1]
assert replace_first([]) == []

print("The mission is done! Click 'Check Solution' to earn rewards!")