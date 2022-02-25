# Вариант 20.
# Из заданной строки отобразить только символы нижнего регистра. Использовать
# библиотеку string. Строка 'In PyCharm, you can specify third-party standalone applications and
# run them as External Tools'.

from string import ascii_lowercase

L = 'In PyCharm, you can specify third-party standalone applications and run them as External Tools'

letters = [i for i in L if i in ascii_lowercase]
print(letters)

