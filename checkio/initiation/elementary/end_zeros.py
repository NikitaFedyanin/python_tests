"""
Попробуйте выяснить какое количество нулей содержит данное число в конце.
"""

def end_zeros(a: int) -> int:
    number = list(str(a))
    number.reverse()
    count = 0
    for i in number:
        if int(i) != 0:
            break
        else:
            count += 1
    return count


print("Example:")
print(end_zeros(10))

# These "asserts" are used for self-checking
assert end_zeros(0) == 1
assert end_zeros(1) == 0
assert end_zeros(10) == 1
assert end_zeros(101) == 0
assert end_zeros(245) == 0
assert end_zeros(100100) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")
