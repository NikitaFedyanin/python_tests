def checkio(data: list) -> list:
    """
    нахождение НЕ уникальных чисел в массиве
    :param data: массив чисел
    :return: массив не уникальных чисел
    """

    global result_list
    result_list = []
    for number in data:
        if data.count(number) != 1:
            result_list.append(number)

    return result_list


if __name__ == "__main__":
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")
