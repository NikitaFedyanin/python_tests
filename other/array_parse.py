"""Парсинг вложенных списков в 1"""


def flat_list(array):
    global stop
    result = []
    while True:
        for elem in array:
            if type(elem) == list:
                for el in elem:
                    result.append(el)
            else:
                result.append(elem)
        stop = True
        for el in result:
            if type(el) == list:
                stop = False
        if stop:
            break
        array.clear()
        for e in result:
            array.append(e)
        result.clear()
    return result



if __name__ == '__main__':
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')
