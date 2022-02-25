# Вариант 20.
# В последовательности на n целых элементов в первой ее половине найти
# количество положительных элементов.
import random
import math

N = int(input('Введите кол-во элементов последовательности: '))
arr = [random.randint(-10, 10) for x in range(N)]
print('Последовательность:', (arr))
l = math.floor(len(arr)/2)

arr2 = [arr[x] for x in range(l)]

arr3 = [n for n in arr2 if n >= 0]
print('Количество положительных элементов в первой половине: ',  len(arr3))