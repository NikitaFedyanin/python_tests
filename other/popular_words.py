def popular_words(text: str, words: list) -> dict:
    lower_text = text.lower()
    popular = {}
    all_words = lower_text.replace('\n', ' ').split(' ')
    for word in words:
        popular.update({word: all_words.count(word)})
    sorted_by_value = sorted(popular.items(), key=lambda kv: kv[1], reverse=True)
    return dict(sorted_by_value)


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")