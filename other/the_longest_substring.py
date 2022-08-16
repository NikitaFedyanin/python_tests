def long_repeat(line):
    """
        Нахождение самого большого повторения латинских букв в строке
    """
    global count, letters_list
    letters_list = ''
    count = 0

    for i in range(0, len(line)-1):
        letters_list += line[i]

        if (i == len(line) - 2) and (line[i + 1] == line[i]):
            letters_list += line[i+1]

            if len(letters_list) > count:
                count = len(letters_list)

        if line[i+1] == line[i]:
            continue
        else:
            if len(letters_list) > count:
                count = len(letters_list)
            letters_list = ''

    if len(letters_list) > count:
        count = len(letters_list)

    return count


if __name__ == '__main__':
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('hjhjhjhjhkkkkklllhhjjhhjjhhjjhhjjoooooooooo') == 10, "Fourth"
    assert long_repeat('kkkkkooooooffffggikgoerigjerogjnergrijrgllllllllllhhhhhhhhhhhhhhhggfdgdfg') == 15, "Fifth"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
