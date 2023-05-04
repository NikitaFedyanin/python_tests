"""
Дана последовательность строк. Вам нужно определить наиболее часто встречаемую строку в последовательности.
"""


def most_frequent(data: list) -> str:
    # your code here
    data_dict = {data.count(i): i for i in data}
    return data_dict[max(data_dict)]


print("Example:")
print(most_frequent(["a", "b", "c", "a", "b", "a"]))

# These "asserts" are used for self-checking
assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"
assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"

print("The mission is done! Click 'Check Solution' to earn rewards!")
