# Дано вещественное число X и целое число N (> 0).
# Найти значение выражения
# 1 - X 2 /(2!) +X 4 /(4!) - ... + (-1) N -X 2*N /((2-N)!)
# (N! = 12 ...N). Полученное число является приближенным
# значением функции cos в точке X. Вариант 20.

import math
N = input("Количество слагаемых: ")
while type(N) != int:                                   # обработка исключений
    try:
        N = int(N)
    except ValueError:
        print("Неправильно ввели!")
        N = int(input("Количество слагаемых: "))

x = input("Введите вевщественное число: ")
while type(x) != float:                                   # обработка исключений
    try:
        x = float(x)
    except ValueError:
        print("Неправильно ввели!")
        x = float(input("Введите число: "))

num1 = 1
res = 1
while num1 < N:
    num2 = (-1) ** num1
    num3 = (x ** (2 * num1)) / (math.factorial(2 * num1))
    num4 = num2 * num3
    res += num4
    num1 += 1
print('Значение выражения равно: ', res)
