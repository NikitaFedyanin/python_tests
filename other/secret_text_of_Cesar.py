def to_encrypt(text, delta):
    """
    Шифр Цезаря
    :param text:
    :param delta:
    :return:
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shiphr = ''
    for letter in text:
        if letter.isalpha():
            new_index = alphabet.index(letter) + delta
            if new_index > len(alphabet):
                new_letter = alphabet[new_index - len(alphabet)]
            else:
                new_letter = alphabet[new_index]
            shiphr = shiphr + new_letter
        else:
            shiphr = shiphr + letter
    return shiphr


if __name__ == '__main__':
    print("Example:")
    print(to_encrypt('abc', 10))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")
