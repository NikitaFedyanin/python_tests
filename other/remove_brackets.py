"""
Перед решением этой миссии можете попробовать решить миссию "Brackets" .

Ваша задача восстановить баланс открытых и закрытых скобок методом удаления ненужных, при этом использовать нужно
 минимальное количеством удалений.

В переданной строке могут использоваться только 3 типа скобок (), [] и {}.

Круглую скобку может закрывать только круглая скобка. Т.е. в этом выражении "(}" - баланса скобок нет. В пустой строке,
 т.е. в строке не содержащей ни одной скобки - баланс скобок есть, но при этом удаление всех скобок не является
 оптимальным решением.

Если правильных ответа больше одного, то выбран должен быть тот, у которого первый убираемый символ находится ближе к
началу. Например для варианта "[(])" правильным ответом будет "()", т.к. убираемые квадратные скобки находятся ближе
к началу строки

Input: Строка, состоящая из символов (){}[]

Output: Строка, состоящая из символов (){}[]
"""
import re

start_brackets = ['[', '{', '(']
end_brackets = [']', '}', ')']
check_start_brackets = {"{": "}", "[": "]", "(": ")"}
check_end_brackets = {"}": "{", "]": "[", ")": "("}


def is_balance(line):
    for i in range(len(line)):
        line = re.sub(r'(?:\(\)|\{\}|\[\])', "", line)
    return not bool(line)


def escape(bracket, line, is_start):
    count = 1
    check_dict = check_start_brackets if is_start else check_end_brackets
    for i in line:
        if i == check_dict[bracket]:
            count -= 1
        elif i == bracket:
            count += 1
        if count == 0:
            return True


def start_check(line):
    new_line = ''
    reversed(line)
    for i, v in enumerate(line):
        if v in start_brackets:
            result = escape(v, line[i + 1:], is_start=True)
        elif v in end_brackets:
            result = escape(v, list(reversed(line))[len(line) - i:], is_start=False)
        if result:
            new_line += v
    return new_line


def remove_brackets(line: str) -> str:
    # your code here
    line = start_check(line)
    while not is_balance(line):
        line = re.sub(r'(?:\(\]|\(\}|\[\)|\[\}|\{\)|\{\])', lambda x: x[0][0], line)
        line = start_check(line)
    return line


if __name__ == "__main__":
    print(remove_brackets("[[{}()]]([{])}(]{[[[[]]{]]]((())){}({})"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert remove_brackets("(()()") == "()()"
    assert remove_brackets("[][[[") == "[]"
    assert remove_brackets("[[(}]]") == "[[]]"
    assert remove_brackets("[[{}()]]") == "[[{}()]]"
    assert remove_brackets("[[[[[[") == ""
    assert remove_brackets("[[[[}") == ""
    assert remove_brackets("") == ""
    assert remove_brackets("[(])") == "()"
    print("Coding complete? Click 'Check' to earn cool rewards!")
