"""
Я начал кормить одного из голубей. Через минуту прилетело еще два,
 и еще через минуту прилетело еще три голубя. Затем 4
  и так далее (Пр: 1+2+3+4+...). Одной порции корма хватает одному голубю на минуту.
  В случае если еды не хватает на всех птиц, то сначала едят те голуби, что прилетели ранее.
   Голуби - это вечно голодные птицы и они будут есть и есть без остановки.
   Если у меня есть N порций корма, то сколько голубей я смогу покормить хотя бы по разу?
"""


def checkio(number):
    eat = number
    birds = 0
    full = 0
    for i in range(1, number + 1):
        if eat <= 0:
            break
        birds += i
        for j in range(birds):
            eat -= 1
            if eat >= 0 and j >= full:
                full += 1
    return full


print(checkio(10000000))

# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert checkio(1) == 1, "1st example"
#     assert checkio(2) == 1, "2nd example"
#     assert checkio(5) == 3, "3rd example"
#     assert checkio(10) == 6, "4th example"
