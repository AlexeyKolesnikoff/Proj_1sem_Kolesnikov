# Вариант 20
# Из текстового файла (writer.txt) выбрать фамилии писателей, посчитать
# количество фамилий. Создать новый файл, в котором выполнить замену
# слова "роман" на слово "произведение"

import re

m = re.compile(r'^[А-ЯЁа-яё]+', re.M)
with open('writer.txt', 'r', encoding = 'utf-8') as f:
    text = f.read()
    list1 = m.findall(text)

    p = re.sub("роман", "произведение", text)

with open('writer2.txt', 'w', encoding = 'utf-8') as f:
    text2 = f.write(p)

list1.pop(0)
print(list1)
print(len(list1))