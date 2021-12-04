# Дан список размера N и целые числа K и L (1 < K < L < N ). Найти среднее
# арифметическое элементов список с номерами от K до L включительно.
import random

arr = []

N = int(input("Введите кол-во элементов в списке: "))
K = int(input("Введите число K: "))
L = int(input('Введите число L: '))

for i in range(N):                                  # Находим первоначальный список
    arr.append(random.randint(K, L))
    arr.sort()
print("Первоначальный список: ", arr)

num = 0
res = 0

for i in range(len(arr)):                            # Находим сумму всех элементов и их кол-во
    if (i >= K-1) and (i <= L-1):
        res += arr[i]
        num += 1
    else:
        continue

print("Среднее арифметическое элементов списка: ", (res / num))


