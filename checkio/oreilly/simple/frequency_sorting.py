"""
Отсортируйте данный список таким образом, чтобы его элементы оказались в порядке убывания частоты их появления,
 то есть по количеству раз, которое они появляются в элементах. Если два элемента имеют одинаковую частоту,
  они должны оказаться в своем естественном порядке. Например [5, 2, 4, 1, 1, 1, 3] ==> [1, 1, 1, 2, 3, 4, 5].
"""

from collections.abc import Iterable


def frequency_sorting(numbers: list[int]) -> Iterable[int]:
    new_list = []
    frequency_dict = {}
    for count, value in sorted([(numbers.count(i), i) for i in numbers], reverse=True):
        if frequency_dict.get(count):
            frequency_dict.get(count).append(value)
        else:
            frequency_dict[count] = [value]

    for k, v in frequency_dict.items():
        new_list += sorted(v)

    return new_list


print("Example:")
print(list(frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3, 5, 5, 5, 5])))

# These "asserts" are used for self-checking
assert list(frequency_sorting([1, 2, 3, 4, 5])) == [1, 2, 3, 4, 5]
assert list(frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3])) == [
    4,
    4,
    4,
    3,
    3,
    11,
    11,
    7,
    13,
]

print("The mission is done! Click 'Check Solution' to earn rewards!")
