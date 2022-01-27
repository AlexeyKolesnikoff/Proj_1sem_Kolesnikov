# Из предложенного текстового файла (text18-20.txt) вывести на экран его содержимое,
# количество символов в тексте. Сформировать новый файл, в который поместить строку
# наибольшей длины.
t = 0
arr1 = []
f2 = open('text18-2.txt', 'w', encoding='UTF-8')
for i in open('text18-20.txt', encoding='UTF-8'):
    print(i, end ='')
    arr1.append(i)
    max_string = max(arr1, key=len)
    for j in i:
        if j == ' ':
            continue
        t += 1
f2.writelines(max_string)
print('\n')
print('Количество символов в тексте: ', t)
f2.close()



