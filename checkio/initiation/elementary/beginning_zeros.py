"""
Вам дана строка состоящая только из цифр. Вам нужно посчитать сколько нулей ("0") находится в начале строки
"""


def beginning_zeros(a: str) -> int:
    # your code here
    count = 0
    for i in a:
        if i == "0":
            count += 1
        else:
            break
    return count


print("Example:")
print(beginning_zeros("10"))

# These "asserts" are used for self-checking
assert beginning_zeros("100") == 0
assert beginning_zeros("001") == 2
assert beginning_zeros("100100") == 0
assert beginning_zeros("001001") == 2
assert beginning_zeros("012345679") == 1
assert beginning_zeros("0000") == 4

print("The mission is done! Click 'Check Solution' to earn rewards!")
