"""
Имея список элементов, создайте и верните список, элементы которого являются списками, которые содержат последовательные
 серии одинаковых элементов исходного списка. Обратите внимание, что элементы, которые не дублируются в исходном списке,
  должны в результате стать одноэлементными списками, чтобы каждый элемент был включен в итоговый список списков.
"""


def group_equal(els):
    result = []
    sub_mass = []

    for i in els:
        if not sub_mass or i == sub_mass[0]:
            sub_mass.append(i)
        else:
            result.append(sub_mass)
            sub_mass = [i]
    if sub_mass:
        result.append(sub_mass)
    return result


print(group_equal([1, 1, 4, 4, 4, "hello", "hello", 4]))

if __name__ == '__main__':
    print("Example:")
    print(group_equal([1, 1, 4, 4, 4, "hello", "hello", 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert group_equal([1, 1, 4, 4, 4, "hello", "hello", 4]) == [[1, 1], [4, 4, 4], ["hello", "hello"], [4]]
    assert group_equal([1, 2, 3, 4]) == [[1], [2], [3], [4]]
    assert group_equal([1]) == [[1]]
    assert group_equal([]) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
