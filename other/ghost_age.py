"""
После множества экспериментов, Никола кажется начел взаимосвязь. На каждый "день рождения",
степень прозрачности привидения уменьшается на количество единиц,
равное его возрасту, если возраст есть одно из чисел Фибоначчи , иначе увеличивается на единицу.
"""


def checkio(opacity):
    current_opacity = 10000
    age = 0

    def is_fibonachi(age):
        is_fibo = False
        fibo_mass = [0, 1, 1]
        if age == 1 or age == 2:
            return True
        while not is_fibo:
            fibo_mass.append(fibo_mass[-1] + fibo_mass[-2])
            if fibo_mass[-1] == age:
                is_fibo = True
            if fibo_mass[-1] > age:
                break
        return is_fibo

    for i in range(1, 5001):
        if is_fibonachi(i):
            current_opacity -= i
        else:
            current_opacity += 1
        age = i
        if current_opacity == opacity:
            break
    return age

print(checkio(7991))
# These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     assert checkio(10000) == 0, "Newborn"
#     assert checkio(9999) == 1, "1 year"
#     assert checkio(9997) == 2, "2 years"
#     assert checkio(9994) == 3, "3 years"
#     assert checkio(9995) == 4, "4 years"
#     assert checkio(9990) == 5, "5 years"
