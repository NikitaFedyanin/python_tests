"""
Разделите строку на пары из двух символов.
Если строка содержит нечетное количество символов,
 пропущенный второй символ последней пары должен быть заменен подчеркиванием ('_').
"""
from typing import Iterable


def split_pairs(text: str) -> Iterable[str]:
    # your code here
    result = []
    tmp_part = ""
    for char in text:
        tmp_part += char
        if len(tmp_part) == 2:
            result.append(tmp_part)
            tmp_part = ""
    if tmp_part:
        result.append(f"{tmp_part}_")
    return result


print("Example:")
print(list(split_pairs("abcd")))

assert list(split_pairs("abcd")) == ["ab", "cd"]
assert list(split_pairs("abc")) == ["ab", "c_"]
assert list(split_pairs("abcdf")) == ["ab", "cd", "f_"]
assert list(split_pairs("a")) == ["a_"]
assert list(split_pairs("")) == []

print("The mission is done! Click 'Check Solution' to earn rewards!")