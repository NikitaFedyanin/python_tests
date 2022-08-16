"""На вход функции дан массив datetime объектов — это дата и время нажатия на кнопку.
Вашей задачей является определить, как долго горела лампочка. Массив при этом всегда отсортирован по возрастанию,
 в нем нет повторяющихся элементов и количество элементов всегда четное число (это значит, что лампочка,
 в конце концов, будет выключена).
"""
from datetime import datetime
from typing import List


def sum_light(els: List[datetime]) -> int:
    """
        how long the light bulb has been turned on
    """
    total_light = 0
    on = None
    for index, action in enumerate(els):
        if index % 2 == 0:
            on = action
        else:
            total_light += (action.timestamp() - on.timestamp())
    return int(total_light)


if __name__ == '__main__':

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ]) == 1220

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
        datetime(2015, 1, 12, 11, 10, 10),
        datetime(2015, 1, 12, 12, 10, 10),
    ]) == 4820

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 1),
    ]) == 1

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 13, 11, 0, 0),
    ]) == 86410

    print("The first mission in series is completed? Click 'Check' to earn cool rewards!")