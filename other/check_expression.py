"""
Дано выражение с цифрами, скобками и операторами. В данной задаче важны только скобки. Скобки представлены в трех
вариациях: "{}" "()" и "[]". Скобки используются, чтобы определить порядок применения операторов или ограничить
участок выражения. Если скобка открывается, то она должна закрываться скобкой того же типа. Участки ограниченные
одной парой скобок, не должны пересекаться с участками других скобок. В этой задаче, вам необходимо определить
правильное ли выражение или нет, основываясь на расположении скобок. И не обращайте внимание на операторы и операнды
"""
import re


def checkio(expression):
    re_check = re.compile(r'(?:\((?:[0-9-*/+]+|)\)|\{(?:[0-9-*/+]+|)\}|\[(?:[0-9-*/+]+|)\])')
    result = False

    while re_check.search(expression):
        expression = re_check.sub('', expression)
    if not re.search(r'(?:\(|\)|\{|\}|\[|\])', expression):
        result = True
    return result


print(checkio("({[3]})-[4/(3*{1001-1000}*3)/4]"))

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("({[3]})-[4/(3*{1001-1000}*3)/4]") == False, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
