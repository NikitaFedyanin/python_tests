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


def sum_light(els: List[datetime], start_watching: Optional[datetime] = None, end_watching: Optional[datetime] = None) -> int:
    """
    how long the light bulb has been turned on
    """
    start_watching = start_watching if start_watching else datetime(1970, 1, 1, 0, 0)
    end_watching = end_watching if end_watching else datetime(9999, 12, 31, 0, 0)
    total_seconds = 0
    switchers = []
    switcher = []
    for item in els:
        switcher.append(item)
        if len(switcher) == 2:
            switchers.append(switcher)
            switcher = []
    if switcher:
        switchers.append([switcher[0], datetime(9999, 12, 31, 23, 59, 59)])
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


if __name__ == "__main__":
    print("Example:")
    print(
        sum_light([
datetime(2015, 1, 12, 10, 0, 0),
datetime(2015, 1, 12, 10, 0, 10),
datetime(2015, 1, 12, 11, 0, 0),
datetime(2015, 1, 13, 11, 0, 0)
])
    )

