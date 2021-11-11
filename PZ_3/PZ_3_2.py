# Даны два числа. Вывести вначале большее, а затем меньшее из них.
# Вариант 20.

a = input("Введите первое число: ")

while type(a) != int:                                   # обработка исключений для первого числа
    try:
        a = int(a)
    except ValueError:
        print("Неправильно ввели!")
        a = int(input("Введите первое число: "))

b = input("Введите второе число: ")

while type(b) != int:                                   # обработка исключений для второго числа
    try:
        b = int(b)
    except ValueError:
        print("Неправильно ввели!")
        b = int(input("Введите второе число: "))

if a > b:
    print(a, b)
else:
    print(b, a)

