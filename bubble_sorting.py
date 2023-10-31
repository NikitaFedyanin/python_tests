my_list = [3, 2, 1, 6, 9, 8, 7, 2, 9, 9, 34, 67]

for i in range(len(my_list)):
    for j in range(len(my_list) - i - 1):
        if my_list[j] > my_list[j + 1]:
            my_list[j + 1], my_list[j] = my_list[j], my_list[j + 1]


print(my_list)
