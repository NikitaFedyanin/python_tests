"""
Помогите Стефану создать программный модуль для перевода времени представленного в нормальном виде,
в двоичную Морзе-форму. Взгляните на иллюстрацию, Серые кружки значат "включено", а белые - "выключено". Каждая цифра
 в написании времени представлена разным количеством бинарных знаков. Первая цифра в "часах" состоит из двух знаков,
 тогда как вторая цифра -- из четырех. Первая цифра "минут" и "секунд" состоят из трех знаков и вторые цифры --
 из четырех.Каждая цифра должна быть переведена в двоичный вид. Затем замените каждую единицу (1) на тире ("-")
 и каждый ноль (0) на точку (".").
"""


def checkio(time_string: str) -> str:
    hour = '{:0>2}'.format(time_string.split(':')[0])
    minute = '{:0>2}'.format(time_string.split(':')[1])
    second = '{:0>2}'.format(time_string.split(':')[2])

    result = '{:.>2} {:.>4} : {:.>3} {:.>4} : {:.>3} {:.>4}'.format(
        bin(int(hour[0])).replace('0b', '').replace('0', '.').replace('1', '-'),
        bin(int(hour[1])).replace('0b', '').replace('0', '.').replace('1', '-'),
        bin(int(minute[0])).replace('0b', '').replace('0', '.').replace('1', '-'),
        bin(int(minute[1])).replace('0b', '').replace('0', '.').replace('1', '-'),
        bin(int(second[0])).replace('0b', '').replace('0', '.').replace('1', '-'),
        bin(int(second[1])).replace('0b', '').replace('0', '.').replace('1', '-'),
    )
    return result


print(checkio("10:37:49"))
if __name__ == '__main__':
    print("Example:")
    print(checkio("10:37:49"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"
    print("Coding complete? Click 'Check' to earn cool rewards!")
