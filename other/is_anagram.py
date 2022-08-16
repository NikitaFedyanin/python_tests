"""
Является ли переданное слово анаграммой
"""
def verify_anagrams(first_word, second_word):
    is_anagram = True
    second = second_word.replace(' ', '').lower()
    first = first_word.replace(' ', '').lower()
    if len(second) != len(first):
        return False
    for i in second:
        if i not in first:
            is_anagram = False
        first = first.replace(i, '', 1)

    return is_anagram

print(verify_anagrams("Kings Lead Hat", "Talking Heads"))
# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
#     assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
#     assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
#     assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"

