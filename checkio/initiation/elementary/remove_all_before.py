"""
Не все элементы важны. Вам нужно удалить из список все элементы до указаного
На примере мы имеем список [1, 2, 3, 4, 5] где нужно было удалить все элементы до 3 - 1 и 2 соответственно.

Есть два ньюанса: (1) если в списке нет элемента до которого нужно удалить остальные элементы,
 то список не должен измениться. (2) если list пустой, то он должен остаться пустым.
"""
from collections.abc import Iterable


def remove_all_before(items: list, border: int) -> Iterable:
    # your code here
    if not items or border not in items:
        return items
    return items[items.index(border):]


print("Example:")
print(list(remove_all_before([1, 2, 3, 4, 5], 3)))

# These "asserts" are used for self-checking
assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
assert list(remove_all_before([], 0)) == []
assert list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [
    7,
    7,
    7,
    7,
    7,
    7,
    7,
    7,
    7,
]

print("The mission is done! Click 'Check Solution' to earn rewards!")