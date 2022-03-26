# В матрице найти сумму элементов первых двух строк
# Вариант 20

import random
i = 4
j = 4
matrix = [[random.randrange(1,10) for y in range(i)] for x in range(j)]

a = sum(matrix[i-4])
b = sum(matrix[i-3])

print("Исходная матрица: ", matrix)
print('Сумма элементов первых двух строк: ', a+b)