"""
Дана квадратная матрица размера NxN (4≤N≤10). Необходимо проверить есть ли здесь последовательность 4
или более одинаковых цифр. Последовательность должна неразрывно располагаться горизонтально,
вертикально или по диагоналям (основным и дополнительным).

find-sequence
Входные данные: Матрица, как список (list) списков с целыми числами.

Выходные данные: Есть ли здесь последовательность, как булево значение (bool).
"""
import re
from typing import List


def checkio(matrix: List[List[int]]) -> bool:
    matrix = [[str(j) for j in i] for i in matrix]
    symbols = re.compile(f'(?:{"|".join({str(j) + "{4}" for i in matrix for j in i})})')
    columns = [[] for i in matrix]
    for line in matrix:
        for i, column in enumerate(line):
            columns[i].append(str(column))
    for column in columns:
        if symbols.search(''.join(column)):
            return True
    for line in matrix:
        if symbols.search(''.join(line)):
            return True
    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True
    print('All Done! Time to check!')
