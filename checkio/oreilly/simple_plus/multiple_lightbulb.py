"""
В третьей миссии из серии о лампочках я хочу выделить отдельно процесс, а отдельно период наблюдения за этим процессом.

В предыдущей миссии был введен параметр start_watching, а в этой – end_watching,
 который указывает время окончания наблюдения. Если он не передан, миссия работает,
  как и в предыдущей версии, без ограничения времени наблюдения.

Еще одно изменение в том, что количество элементов (нажатий на кнопку) может быть нечетным
(в предыдущей миссии серии - количество элементов всего было четным).
При этом обязательно присутствуют параметры начала и окончания просмотра.
"""
# Taken from mission Lightbulb Start Watching
from datetime import datetime
from typing import List, Optional


def calculate_watching(switchers, start_watching=None, end_watching=None):
    start_watching = start_watching if start_watching else datetime(1970, 1, 1, 0, 0)
    end_watching = end_watching if end_watching else datetime(9999, 12, 31, 0, 0)
    total_seconds = 0
    for on, off in switchers:
        if start_watching >= on and end_watching <= off:
            total_seconds += (end_watching - start_watching).total_seconds()
        elif on <= end_watching <= off:
            total_seconds += (end_watching - on).total_seconds()
        elif on <= start_watching <= off:
            total_seconds += (off - start_watching).total_seconds()
        elif start_watching <= on and off <= end_watching:
            total_seconds += (off - on).total_seconds()
    return total_seconds


def intersection(switchers):
    total_switchers = []
    checked = []
    while switchers:
        tmp = switchers.pop(0)
        if tmp in checked:
            continue
        for i in switchers:
            if i not in checked and (tmp[0] <= i[0] <= tmp[1] or tmp[0] <= i[1] <= tmp[1]):
                tmp = (min(i + tmp), max(i + tmp))
                checked.append(i)
        total_switchers.append(tmp)
    return total_switchers


def sum_light(els: List[datetime], start_watching: Optional[datetime] = None,
              end_watching: Optional[datetime] = None) -> int:
    """
    how long the light bulb has been turned on
    """
    total_switchers = []
    for i in range(1, len(els) + 1):
        if i == 1:
            switcher_list = list(filter(lambda x: isinstance(x, datetime), els))
        else:
            switcher_list = [j[0] for j in els if isinstance(j, tuple) and j[1] == i]
        if len(switcher_list) % 2 == 1:
            switcher_list.append(datetime(9999, 12, 31, 23, 59, 59))
        total_switchers += list(zip(switcher_list[::2], switcher_list[1::2]))
    return calculate_watching(intersection(total_switchers), start_watching, end_watching)


if __name__ == "__main__":
    print("Example:")
    print(
        sum_light([
            (datetime(2015, 1, 12, 10, 0, 10), 3),
            datetime(2015, 1, 12, 10, 0, 20),
            (datetime(2015, 1, 12, 10, 0, 30), 3),
            (datetime(2015, 1, 12, 10, 0, 30), 2),
            datetime(2015, 1, 12, 10, 0, 40),
            (datetime(2015, 1, 12, 10, 0, 50), 2),
            (datetime(2015, 1, 12, 10, 1, 0), 3),
            (datetime(2015, 1, 12, 10, 1, 20), 3),
        ]) == 60
    )
