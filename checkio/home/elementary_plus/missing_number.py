"""
You are given a sequence of integers, which are elements of arithmetic progression -
the difference between the consecutive elements is constant.
But this sequence is unsorted and one element is missing...good luck!
"""


def missing_number(items: list[int]) -> int:
    delta_list = []
    items.sort()
    my_delta = None
    for i, v in enumerate(items[1:]):
        delta_list.append(v - items[i])
    delta_list = set(delta_list)
    for delta in delta_list:
        check_mass = []
        for i, v in enumerate(items[1:]):
            check_mass.append((v - items[i]) == delta or (v - items[i]) == (delta * 2))
        if all(check_mass):
            my_delta = delta
            break
    for i, v in enumerate(items[1:]):
        if v - items[i] == (my_delta * 2):
            return items[i] + my_delta
    return 0


print("Example:")
assert missing_number([5, 25, 30, 20, 15]) == 10

print("The mission is done! Click 'Check Solution' to earn rewards!")
