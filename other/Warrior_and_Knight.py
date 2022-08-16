class Warrior:
    health = 50
    atack = 5
    is_alive = True


class Knight(Warrior):
    atack = 7


def fight(unit_1, unit_2):
    while True:
        unit_2.health = unit_2.health - unit_1.atack
        unit_2.is_alive = True if unit_2.health >= 0 else False
        if not unit_2.is_alive:
            return True
        unit_1.health = unit_1.health - unit_2.atack
        unit_1.is_alive = True if unit_1.health >= 0 else False
        if not unit_1.is_alive:
            return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")
