"""
Формат ввода
В единственной строке входных данных содержится непустая строка. Гарантируется, что эта строка является результатом корректного RLE-сжатия некоторой строки.
Формат вывода
Выведите длину исходной строки.
Пример 1
Ввод	Вывод
A15BA5  21

"""

inp_string = input()
result_dict = {}

count = ''
pass_string = ''
for i in inp_string:
    pass_string += i

    if i.isalpha():
        next_items = inp_string.replace(pass_string, '', 1)
        if not next_items:
            count = 1 if not count else count
            if i in result_dict.keys():
                result_dict.update({i: int(count) + result_dict[i]})
            else:
                result_dict.update({i: int(count)})
        for j in range(len(next_items)):
            if next_items[j].isdigit():
                count += next_items[j]
            if next_items[j].isalpha() or j == len(next_items)-1:
                count = 1 if not count else count
                if i in result_dict.keys():
                    result_dict.update({i: int(count) + result_dict[i]})
                else:
                    result_dict.update({i: int(count)})
                count = ''
                break
result = sum(result_dict.values())

print(result)
