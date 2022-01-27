# Вариант 20.
# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Минимальный элемент:
# Числа кратные трем:
# Количество чисел кратных трем:

l = ['-99 6 12 -36 20 45 100 -15']
f1 = open('data_1.txt', 'w', encoding='UTF-8')
f1.writelines(l)
f1.close()

f2 = open('data_2.txt', 'w', encoding='UTF-8')
f2.write('Исходные данные: ')
f2.writelines(l)
f2.close()

f1 = open('data_1.txt')
k = f1.read()
k = k.split()
for i in range(len(k)):
    k[i] = int(k[i])
f1.close()

f1 = open('data_1.txt')
max = 0
min = 0
t = 0
for i in range(len(k)):
    max = max if max > k[i] else k[i]
    min = min if min < k[i] else k[i]
    if k[i] % 3 == 0:
        t += 1

f2 = open('data_2.txt', 'a', encoding='UTF-8')
f2.write('\n')
f2.writelines('Количество элементов: ')
f2.writelines(str(len(k)))
f2.write('\n')
f2.writelines('Максимальный элемент: ')
f2.writelines(str(max))
f2.write('\n')
f2.writelines('Минимальный элемент: ')
f2.writelines(str(min))
f2.write('\n')
f2.writelines('Количество чисел кратных трем: ')
f2.writelines(str(t))
f2.write('\n')
print('Количество элементов: ', len(k))
print('Максимальный элемент: ', max)
print('Минимальный элемент: ', min)
print('Количество чисел кратных трем: ', t)