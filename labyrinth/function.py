import copy
import time
import random


def short_way(array):
    """
    Парсинг всех пройденных координат
    :param array: массив координат
    :return: путь без повторений (кратчайший от переданного)
    """
    result = []
    while True:
        i = 0
        j = 0
        stop = True
        for i in range(len(array)):
            if array.count(array[i]) > 1:
                stop = False
                value = array[i]
                start_index = array.index(value)
                array.reverse()
                end_index = array.index(value)
                array.reverse()
                for_cut = array[start_index: -end_index]
                for j in range(len(array)):
                    if array[j] not in for_cut:
                        result.append(array[j])
                    else:
                        for_cut.pop(0)
                result.insert(start_index, value)
                if not stop:
                    break
        if i == len(array) - 1 and stop:
            break
        array = result[:]
        result.clear()
    return array


def get_way(coord_list):
    """
    получение буквенного пути
    :param coord_list: координаты маршрута
    :return: буквенный маршрут
    """
    route = []
    before = (1, 1)
    move = {(1, 0): "S", (-1, 0): "N", (0, -1): "W", (0, 1): "E"}
    for i in coord_list:
        diff_y = i[0] - before[0]
        diff_x = i[1] - before[1]
        diff = (diff_y, diff_x)
        if diff in move.keys():
            route.append(move[diff])
        before = i
    return route


def show_way(map, way):
    """
    Отображение всего пути
    :param map: карта лабиринта
    :param way: путь в координатах
    """
    print_map = copy.deepcopy(map)
    for i in range(len(print_map)):
        for j in range(len(print_map[i])):
            if (i, j) in way or (i, j) == (1, 1):
                print_map[i][j] = ' @ '
            else:
                print_map[i][j] = ' . ' if print_map[i][j] == 1 else '   '
        print_map[i][-1] = print_map[i][-1] + '\n'
        print_map[i] = ''.join(print_map[i])
    print_map = ''.join(print_map)
    print(print_map)


def show_current_position(map, pos):
    """
    Отображение текущей позиции
    :param map: карта лабиринта
    :param pos: текущая позиция
    """
    print_map = copy.deepcopy(map)
    for i in range(len(print_map)):
        for j in range(len(print_map[i])):
            if i == pos[0] and j == pos[1]:
                print_map[i][j] = ' @ '
                continue
            print_map[i][j] = ' . ' if print_map[i][j] == 1 else '   '
        print_map[i][-1] = print_map[i][-1] + '\n'
        print_map[i] = ''.join(print_map[i])
    print_map = ''.join(print_map)
    print(print_map)
    time.sleep(0.1)


def get_right_way(map, pos, last_coord):
    """
    Получение следующего возможного хода, игнорируются стены и обратное направление (если есть путь вперед)
    :param map: карта лабиринта
    :param pos: текущая позиция
    :param last_coord: предыдущая координата
    :return: случайная координата направления пути из возможных
    """
    rand_move = {1: (1, 0), 2: (-1, 0), 3: (0, -1), 4: (0, 1)}
    right_ways = []
    if map[pos[0] + 1][pos[1]] == 0:
        right_ways.append(1)
    if map[pos[0] - 1][pos[1]] == 0:
        right_ways.append(2)
    if map[pos[0]][pos[1] - 1] == 0:
        right_ways.append(3)
    if map[pos[0]][pos[1] + 1] == 0:
        right_ways.append(4)
    if len(right_ways) > 1:
        if last_coord:
            for i in right_ways:
                step = rand_move.get(i)
                next_step = pos[0] + step[0], pos[1] + step[1]
                if next_step == last_coord:
                    right_ways.remove(i)

    return random.choice(right_ways)


def log(func):
    """Декоратор для оформления"""

    def get_params(maze_map):
        print('================================================================')
        print('Начинается построение маршрута')
        print('================================================================')
        way = func(maze_map)

        print('================================================================')
        print('маршрут построен')
        print('================================================================')
        return way

    return get_params


