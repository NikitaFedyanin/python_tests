"""
Дан список состоящий из целых чисел. Ваша задача выяснить сколько раз в нем меняется направление при переходе
от одного числа к другому. Если числа равны, то направление не меняется. В случае, если следующий элемент
отличается от предыдущего - необходимо определить в какую сторону поменялось направление.
"""


def changing_direction(elements: list[int]) -> int:
    result = []
    if len(elements) > 2:
        for i, v in enumerate(elements[1:]):
            delta = v - elements[i]
            if delta != 0 and (not result or (result[-1] > 0) != (delta > 0)):
                result.append(delta)
    return len(result) - 1 if result else 0


print("Example:")
assert changing_direction([6, 6, 6, 4, 1, 2, 5, 9, 7, 8, 5, 9, 4, 2, 6]) == 7

print("The mission is done! Click 'Check Solution' to earn rewards!")
