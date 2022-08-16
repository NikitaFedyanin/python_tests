VOWELS = "aeiouy"
"""
птичий язык
"""

def translate(phrase):
    vowels = 'aeiouy'
    words = phrase.split(' ')
    result = []
    for word in words:
        count = 0
        new_word = ''
        for i in range(len(word)):
            if count >= len(word):
                break
            if word[count] not in vowels:
                new_word += word[count]
                count += 2
                continue
            if word[count] in vowels:
                new_word += word[count]
                count += 3
        result.append(new_word)
    phrase = ' '.join(result)
    return phrase


print(translate("hieeelalaooo"))

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
