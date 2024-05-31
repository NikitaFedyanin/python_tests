# LinkedList или связный список – это структура данных,
# которая в общем случае обеспечивает возможность создать направленную очередь из элементов.
# Каждый элемент такого списка считается узлом.
# В узле указаны его значение и ссылки на предыдущий и/или последующий узлы.
# В линейном связном списке последний элемент списка указывает на NULL
# Разновидностью связных списков является кольцевой (или замкнутый) список.
# Последний элемент кольцевого списка указыавет на первый


# Реализация однонаправленного связного списка с указателем на предыдущий элемент
class LinkedList:

    def __init__(self, value, prev):
        self.value = value
        self.prev = prev


item1 = LinkedList(5, None)
item2 = LinkedList(4, item1)
item3 = LinkedList(5, item2)
item4 = LinkedList(4, item3)
item5 = LinkedList(5, item4)

# закольцовываем
item1.prev = item5


# Задача: написать метод, проверяющий связный список на закольцованность/замкнутость
# В параметры метода передается один любой элемент связного списка
# Метод должен возвращать результат выполнения True/False

def func(item):
    count = 0

    def _exec(value):
        nonlocal count
        if value == item and (count := count + 1) == 2:
            return True
        return _exec(value.prev) if value.prev else False
    return _exec(item)


print('Список замкнутый' if func(item2) is True else 'Список линейный')
