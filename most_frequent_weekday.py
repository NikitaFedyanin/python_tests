"""
Вам дан год как целое число (например, 2001). Вы должны вернуть наиболее частые дни недели в этом году. Результатом
должен быть список дней, отсортированный по порядку дней в неделе (например, [«Понедельник», «Вторник»]).
 Неделя начинается с понедельника.
"""
from datetime import date, timedelta
import calendar


def most_frequent_days(a):
    # your code here
    days_count = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    days_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    result = []
    first_day = date.fromisoformat('{:0>4}-01-01'.format(a))
    while first_day.year == a:
        days_count[first_day.weekday()] = days_count[first_day.weekday()] + 1
        first_day = first_day + timedelta(days=1)
    for k, v in days_count.items():
        if v == max(days_count.values()):
            result.append(days_name[k])
    return result


if __name__ == '__main__':

    # These "asserts" are used for self-checking and not for an auto-testing
    assert most_frequent_days(1084) == ['Tuesday', 'Wednesday']
    assert most_frequent_days(1167) == ['Sunday']
    assert most_frequent_days(1216) == ['Friday', 'Saturday']
    assert most_frequent_days(1492) == ['Friday', 'Saturday']
    assert most_frequent_days(1770) == ['Monday']
    assert most_frequent_days(1785) == ['Saturday']
    assert most_frequent_days(212) == ['Wednesday', 'Thursday']
    assert most_frequent_days(1) == ['Monday']
    assert most_frequent_days(2135) == ['Saturday']
    assert most_frequent_days(3043) == ['Sunday']
    assert most_frequent_days(2001) == ['Monday']
    assert most_frequent_days(3150) == ['Sunday']
    assert most_frequent_days(3230) == ['Tuesday']
    assert most_frequent_days(328) == ['Monday', 'Sunday']
    assert most_frequent_days(2016) == ['Friday', 'Saturday']
    print("Coding complete? Click 'Check' to earn cool rewards!")
