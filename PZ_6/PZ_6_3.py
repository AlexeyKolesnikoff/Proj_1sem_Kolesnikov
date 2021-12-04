# Дан список размера N, все элементы которого, кроме одного, упорядочены по
# убыванию. Сделать список упорядоченным, переместив элемент, нарушающий
# упорядоченность, на новую позицию.

import random
N = int(input("Введите длину массива: "))

arr = []
for i in range (N):
    ran = random.randint(1, 10)                  # Создание массива размера N
    arr.append(ran)

arr = sorted(arr, reverse=True)                  # Отсортированный массив
random_num = random.randint(1, 10)
index_ran = random.randint(0, len(arr) - 1)

arr[index_ran] = random_num
print("Массив - ", arr)                                  # Измененный массив
print(sorted(arr,reverse=True))
