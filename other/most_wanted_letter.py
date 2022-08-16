def checkio(string) -> str:
    """
    нахождение наибольшего вхождения элемента(буквы) в строке
    :param string: строка
    :return: буква, чаще всего встречающаяся в строке
    """
    global letters, count, result
    letters = []
    count = 0
    check_string = string.lower()

    for letter in check_string:
        if letter.isalpha() and letter.islower():
            letter_count = check_string.count(letter)
            if letter_count == count:
                if letter not in letters:
                    letters.append(letter)
            if letter_count > count:
                letters.clear()
                letters.append(letter)
                count = letter_count
    letters.sort()

    return letters[0]


if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
