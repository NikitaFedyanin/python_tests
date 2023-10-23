"""
Проверить все ли символы в строке являются заглавными.
Если строка пустая или в ней нет букв - функция должна вернуть True.
"""


def is_all_upper(text: str) -> bool:
    # your code here
    result = True
    letters = [i for i in text if i.isalpha()]
    if not letters or "".join(letters).isupper():
        return True
    else:
        return False


print("Example:")
print(is_all_upper("ALL UPPER"))

# These "asserts" are used for self-checking
assert is_all_upper("ALL UPPER") == True
assert is_all_upper("all lower") == False
assert is_all_upper("mixed UPPER and lower") == False
assert is_all_upper("") == True
assert is_all_upper("444") == True
assert is_all_upper("55 55 5 ") == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
