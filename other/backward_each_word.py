"""
Требуется обратить порядок букв в каждом слове предоставленной строки, так чтобы слова остались на своих местах.
Входные данные: строка.
Выходные данные: строка.
"""


def backward_string_by_word(text: str) -> str:
    # your code here
    result = ' '.join([i[::-1] for i in text.split(' ')])
    return result


if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")
