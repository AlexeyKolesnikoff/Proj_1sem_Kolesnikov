# Дано целое число N (> 0). Найти сумму 1 1 + 2 2 + ... + N N
# Вариант 20.

N = input("Введите целое число: ")
while type(N) != int:                                   # обработка исключений
    try:
        N = int(N)
    except ValueError:
        print("Неправильно ввели!")
        N = int(input("Введите целое число: "))

res = 0
while N > 0:
    res += N ** N
    N -=1
print ("Значение выражения равно: ", res)

