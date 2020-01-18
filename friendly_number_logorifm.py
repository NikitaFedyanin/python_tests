import math

"""
Вам нужно написать функцию для конвертации числа (аргумент number) используя следующие правила. Для начала,
 необходимо "обрезать" и округлить число до данной базы (аргумент base; по умолчанию 1000). 
 Число должно стать коэффициентом с буквой (или буквами) определяющими степень базы. 
 Коэффициент - это действительное число с определённым числом знаков после точки (аргумент decimals; по умолчанию 0). 
 Вам дан список обозначений степеней (аргумент powers; по умолчанию ['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']). 
 Если дан суффикс (аргумент suffix; по умолчанию ‘’) , то необходимо добавить его в конец результата. 
 Коофицент округляется в сторону нуля (5.6⇒5, -5.6⇒-5), если decimal == 0, в остальных случаях используйте стандартное
  математическое округление. Если данного списка степеней недостаточно, то используйте последний, а дальше, 
  как обычное число. Если необходимое количество знаков после запятой (decimals) больше чем необходимо, то дополняйте
   нулями. И ноль всегда ноль без всяких степеней.
"""


def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    """
    Приведение числа к красивому формату
    """
    minus = ""
    log = 0
    if number < 0:  # Если число отрицательное, то запоминаем минус и вычисляем модуль числа
        minus = "-"
        number = abs(number)
    if number:
        # Вычисление логарифма с учетом "дозволенных" значений в powers
        log = int(math.log(number, base)) if int(math.log(number, base)) < len(powers) else len(powers) - 1
    power = powers[log]
    friend_base = number / math.pow(base, log)
    friend_round = '{0:.{dec}f}'.format(friend_base, dec=decimals) if decimals else math.floor(friend_base)
    return '{minus}{0}{1}{2}'.format(friend_round, power, suffix, minus=minus)


print(friendly_number(0, decimals=3, suffix="th"))

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert friendly_number(102) == '102', '102'
    assert friendly_number(10240) == '10k', '10k'
    assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'
