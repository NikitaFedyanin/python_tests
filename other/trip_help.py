from datetime import datetime


def sun_angle(time):
    """
    Расчет угла солнца над горизонтом по времени
    :param time:
    :return:
    """
    begin = datetime.strptime('06:00', '%H:%M')
    end = datetime.strptime('18:00', '%H:%M')
    time_in = datetime.strptime(time, '%H:%M')
    if begin <= time_in <= end:
        all_seconds = (end - begin).seconds
        seconds_since_begin_to_now = (time_in - begin).seconds
        percent = seconds_since_begin_to_now / all_seconds * 100
        ugol = round(180 / 100 * percent, 2)
        return ugol
    else:
        return "I don't see the sun!"


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
