# Дан целочисленный список размера N. Найти максимальное количество его
# одинаковых элементов.

import random
N = int(input("Введите размер списка: "))

arr = []
for i in range(N):
    ran = random.randint(1, 10)               # Создание массива размерa N
    arr.append(ran)
coin = []
print("Массив: ", arr)
for i in arr:
    coin.append(arr.count(1))
print("Максимальное кол-во одинаковых элементов массива: ", max(coin))