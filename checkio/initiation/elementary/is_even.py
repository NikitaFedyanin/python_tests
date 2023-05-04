"""
Проверить является ли число четным или нет. Ваша функция должна возвращать True если число четное,
 и False если число не четное.
"""


def is_even(num: int) -> bool:
    # your code here
    return not bool(num % 2)


print("Example:")
print(is_even(2))

# These "asserts" are used for self-checking
assert is_even(2) == True
assert is_even(5) == False
assert is_even(0) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
