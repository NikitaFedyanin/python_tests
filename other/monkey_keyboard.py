def count_words(text: str, words: set) -> int:
    """
    Нахождение заданных слов в тексте
    :param text: входной текст
    :param words: заданная последовательность слов
    :return: количество заданных слов в тексте
    """
    global count
    count = 0
    lower_string = text.lower()
    for word in words:
        if word in lower_string:
            count += 1

    return count


if __name__ == '__main__':
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
