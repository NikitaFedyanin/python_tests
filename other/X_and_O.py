from typing import List


def checkio(game_result: List[str]) -> str:
    """
    Проверка выигрыша в крестики нолики
    :param game_result:
    :return:
    """

    if "XXX" in game_result:
        return "X"
    if "OOO" in game_result:
        return "O"
    win_x = ((game_result[0][0], game_result[1][0], game_result[2][0]) == ('X', 'X', 'X') or (
            game_result[0][1], game_result[1][1], game_result[2][1]) == ('X', 'X', 'X') or (
                     game_result[0][2], game_result[1][2], game_result[2][2]) == ('X', 'X', 'X') or (
                     game_result[0][0], game_result[1][1], game_result[2][2]) == ('X', 'X', 'X') or (
                     game_result[0][2], game_result[1][1], game_result[2][0]) == ('X', 'X', 'X'))
    win_o = ((game_result[0][0], game_result[1][0], game_result[2][0]) == ('O', 'O', 'O') or (
        game_result[0][1], game_result[1][1], game_result[2][1]) == ('O', 'O', 'O') or (
                 game_result[0][2], game_result[1][2], game_result[2][2]) == ('O', 'O', 'O') or (
                 game_result[0][0], game_result[1][1], game_result[2][2]) == ('O', 'O', 'O') or (
                 game_result[0][2], game_result[1][1], game_result[2][0]) == ('O', 'O', 'O'))
    if win_x:
        return 'X'
    elif win_o:
        return 'O'
    else:
        return 'D'


if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
