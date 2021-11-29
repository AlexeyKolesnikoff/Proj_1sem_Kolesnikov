# Дан прямоугольник, длины сторон которого равны натуральным числам A и B.
# Составить функцию, которая будет находить на сколько квадратов можно
# разрезать данный прямоугольник, если от него каждый раз отрезать квадрат
# наибольшей площади

def square(length, width):

    res = 0
    while length > 0 and width > 0:
        if width > length:
            width, length = length, width             # меняем местами, если длина меньше ширины
        length -= width
        res += 1
        if length == 1 and width == 1:                # выход из цикла, когда находим квадрат 1х1
            break
    print("Количество квадратов равно", res)

a = int(input("Введите длину прямоугольника: "))
b = int(input("Введите ширину прямоугольника: "))

square(a, b)


