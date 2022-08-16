"""
Компьютерный формат даты и времени обычно выглядит так: 21.05.2018 16:30
Люди предпочитают видеть эту же информацию в более развернутом виде: 21 May 2018 year, 16 hours 30 minutes
Ваша задача - преобразовать дату и время из числового формата и словесно-числовой.
"""

months = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June', '07': 'July',
          '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December'}


def date_time(time: str) -> str:
    # replace this for solution
    str_date = time.split()[0].split('.')
    str_time = time.split()[1].split(':')
    hour_ending = '' if str_time[0].endswith('1') else 's'
    minute_ending = '' if str_time[1].endswith('1') else 's'
    result = f'{int(str_date[0])} {months[str_date[1]]} {str_date[2]} year ' \
             f'{int(str_time[0])} hour{hour_ending} {int(str_time[1])} minute{minute_ending}'
    return result


if __name__ == "__main__":
    print("Example:")
    print(date_time("01.01.2000 00:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert (
            date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
    ), "Millenium"
    assert (
            date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes"
    ), "Victory"
    assert (
            date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes"
    ), "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
