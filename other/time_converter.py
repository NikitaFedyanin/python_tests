def time_converter(time):
    """Конвертер времени"""
    if time.split(':')[0][0] == '0' and time.split(':')[0][1] != '0':
        res = '%s:%s a.m.' % (time.split(':')[0][1], time.split(':')[1])
        return res
    elif time == '00:00':
        return '12:00 a.m.'
    elif time.split(':')[0] == '12':
        return time+' p.m.'
    else:
        convert = time.split(':')[0]
        full = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 00]
        short = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        count = full.index(int(convert))
        return '%s:%s p.m.' % (str(short[count]), time.split(':')[1])


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
