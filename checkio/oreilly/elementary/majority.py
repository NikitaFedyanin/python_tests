"""
We have a list of logic values (bool). Let's check if the majority of elements are True.
Some cases worth mentioning:
1) an empty list should return False;
2) if True-s and False-s have an equal amount, function should return False
"""


def is_majority(items: list[bool]) -> bool:
    true_v, false_v = 0, 0
    for item in items:
        if item:
            true_v += 1
        else:
            false_v += 1
    return bool(items) and true_v > false_v


print("Example:")
print(is_majority([True, True, False, True, False]))

# These "asserts" are used for self-checking
assert is_majority([True, True, False, True, False]) == True
assert is_majority([True, True, False]) == True
assert is_majority([True, True, False, False]) == False
assert is_majority([True, True, False, False, False]) == False
assert is_majority([False]) == False
assert is_majority([True]) == True
assert is_majority([]) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
