n = int(input())
my_list = [input() for i in range(n)]
def funct(numer, x = 256):
    x = [int(i) for i in numer.split('.')]
    y = x[0] * (x**3) + x[1] * (x**2) + x[2] * (x**1) + x[3] * (x**0)
    return y
b = sorted(my_list, key=funct)
print(b)