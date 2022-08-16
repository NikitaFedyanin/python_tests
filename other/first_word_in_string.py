def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    result = ''
    lst = text.split(' ')
    for elm in lst:
        if len(elm) < 1:
            continue
        for letter in elm:
            if letter == ',' or letter == '.':
                if len(result) > 0:
                    return result
                continue
            else:
                result += letter
        if len(result) > 0:
            return result


def more_easy(text):
    text = text.replace(',', ' ').replace('.', ' ').strip()
    text = text.split(' ')
    return text[0]


if __name__ == '__main__':
    print("Example:")
    print(first_word("... and so on ..."))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")
