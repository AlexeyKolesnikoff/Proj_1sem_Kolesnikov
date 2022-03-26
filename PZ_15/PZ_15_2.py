# В матрице найти минимальный и максимальные элементы.
# Вариант 20
import random
arr = []

print("Введите размер матрицы")

i = int(input())
j = int(input())
matrix = [[random.randrange(1,10) for y in range(i)] for x in range(j)]
print('Исходная матрица', matrix)

for i in matrix:
    arr.append(min(i))
print("Минимальный элемент матрицы: ", min(arr))

for i in matrix:
    arr.append(max(i))
print("Максимальный элемент матрицы: ", max(arr))