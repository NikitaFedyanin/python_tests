def checkio(str) -> bool:
    """
    Проверка пароля на сложность
    :param str: строка с паролем
    :return: True - пароль сложный False - пароль не соответствует параметрам
    """

    global length, latin_latter, number, upper_letter, lower_letter
    length = False
    latin_latter = False
    number = False
    upper_letter = False
    lower_letter = False
    for string_element in str:

        length = 10 <= len(str) <= 64

        if not latin_latter:
            latin_latter = string_element.isalpha()

        if not number:
            number = string_element.isdigit()

        if not upper_letter:
            upper_letter = string_element.isupper()

        if not lower_letter:
            lower_letter = string_element.islower()

    result = length and latin_latter and number and upper_letter and lower_letter

    return result


if __name__ == '__main__':
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
