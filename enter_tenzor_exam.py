def checkio(words: str) -> bool:
    """
    Найти в строке с цифрами и словами 3 слова, идущие подряд
    :param words:
    :return:
    """
    main_list = words.split(' ')
    count = []
    a = 0
    for elm in main_list:
        if elm.isalpha():
            count.append(elm)
            if len(count) == 3:
                return True
        else:
            count.clear()
    return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")